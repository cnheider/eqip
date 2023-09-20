#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "heider"
__doc__ = r"""

           Created on 12/19/22
           """

__all__ = [
    "install_requirements_from_file",
    "install_requirements_from_name",
    "append_item_state",
    "is_package_installed",
    "remove_requirements_from_name",
    "strip_item_state",
    "is_package_updatable",
]

import cgi
import ensurepip
import json
import os
import subprocess
import sys

from enum import Enum
from importlib.metadata import Distribution
from pathlib import Path
from typing import Iterable, List, Tuple, Optional, Union
from urllib.error import HTTPError
from urllib.request import (
    Request,
    urlopen,
)  # TODO: should use QgsNetworkAccessManager instead for networking

from packaging import version
from packaging.version import InvalidVersion, Version

# from warg import is_windows # avoid dependency import not standard python pkgs.
CUR_OS = sys.platform
IS_WIN = any(CUR_OS.startswith(i) for i in ["win32", "cygwin"])
IS_MAC = CUR_OS.startswith("darwin")


# @passes_kws_to(subprocess.check_call)
def catching_callable(*args, **kwargs):
    try:
        subprocess.check_call(*args, **kwargs)
    except subprocess.CalledProcessError as e:
        print(e)


SP_CALLABLE = catching_callable  # subprocess.call
DEFAULT_PIP_INDEX = os.environ.get("PIP_INDEX_URL", "https://pypi.org/pypi/")


class InstallStateEnum(Enum):
    """ """

    updatable = "(Updatable)"
    editable = "(Editable)"
    manual = "(Manual)"
    broken = "(Broken)"
    not_installed = "(Not Installed)"


class UpgradeStrategyEnum(Enum):
    """
    eager - all packages will be upgraded to the latest possible version. It should be noted here that pip’s current
    resolution algorithm isn’t even aware of packages other than those specified on the command line, and those
    identified as dependencies. This may or may not be true of the new resolver.

    only-if-needed - packages are only upgraded if they are named in the pip command or a requirement file (i.e,
    they are direct requirements), or an upgraded parent needs a later version of the dependency than is currently
    installed.

    to-satisfy-only (undocumented, please avoid) - packages are not upgraded (not even direct requirements) unless the
    currently installed version fails to satisfy a requirement (either explicitly specified or a dependency).

    This is actually the “default” upgrade strategy when --upgrade is not set, i.e. pip install AlreadyInstalled and pip
    install --upgrade --upgrade-strategy=to-satisfy-only AlreadyInstalled yield the same behavior.
    """

    eager = "eager"
    to_satisfy_only = "to-satisfy-only"
    only_if_needed = "only-if-needed"


# subprocess.Popen(**ADDITIONAL_PIPE_KWS)
# ADDITIONAL_PIPE_KWS = dict(stderr=subprocess.PIPE,stdout=subprocess.PIPE, stdin=subprocess.PIPE)


def get_qgis_python_interpreter_path() -> Optional[Path]:
    """

    :return: The path of the qgis python interpreter
    :rtype: Optional[Path]
    """
    interpreter_path = Path(sys.executable)
    if IS_WIN:  # For OSGeo4W
        try_path = interpreter_path.parent / "python.exe"
        if not try_path.exists():
            try_path = interpreter_path.parent / "python3.exe"
            if not try_path.exists():
                print(f"Could not find python {try_path}")
                return None
        return try_path

    elif IS_MAC:
        try_path = interpreter_path.parent / "bin" / "python"
        if not try_path.exists():
            try_path = interpreter_path.parent / "bin" / "python3"
            if not try_path.exists():
                print(f"Could not find python {try_path}")
                return None
        return try_path

    # QString QStandardPaths::findExecutable(const QString &executableName, const QStringList &paths = QStringList())

    return interpreter_path


def install_requirements_from_file(
    requirements_path: Path,
    upgrade: bool = True,
    upgrade_strategy: UpgradeStrategyEnum = UpgradeStrategyEnum.only_if_needed,
) -> None:
    """
    Install requirements from a requirements.txt file.

    :param upgrade:
    :param upgrade_strategy:
    :param requirements_path: Path to requirements.txt file.
    :rtype: None
    """

    args = ["install", "-r", str(requirements_path)]

    if upgrade:
        args += ["--upgrade"]

    if upgrade_strategy:
        args += ["--upgrade-strategy", upgrade_strategy.value]

    """
  other options:
  
  --index-url
--extra-index-url
--no-index
--find-links
  
  --force-reinstall
  --ignore-installed
  --no-deps
  --ignore-requires-python
  --require-hashes
  --editable
  --pre # Prereleases
  """

    if False:
        import pip

        pip.main(args)

    elif False:
        SP_CALLABLE(["pip"] + args)

    elif True:
        install_pip_if_not_present()

        if is_pip_installed():
            SP_CALLABLE([str(get_qgis_python_interpreter_path()), "-m", "pip", *args])

        else:
            print("PIP IS STILL MISSING!")


def is_pip_installed():
    pip_present = True
    try:
        import pip
    except ImportError:
        pip_present = False
    return pip_present


def install_pip_if_not_present(always_upgrade: bool = True):
    if not is_pip_installed() or always_upgrade:
        if False:
            ensurepip.bootstrap(upgrade=True)
        else:
            SP_CALLABLE(
                [
                    str(get_qgis_python_interpreter_path()),
                    "-m",
                    "ensurepip",
                    "--upgrade",
                ]
            )


"""
import pip

def import_or_install(package):
    try:
        __import__(package)
    except ImportError:
        pip.main(['install', package])    
"""


def pip_installed():
    import subprocess

    pip_check = subprocess.run([str(get_qgis_python_interpreter_path()), "-m", "pip"])
    return not bool(pip_check.returncode)


def is_requirement_installed(requirement_name: str) -> bool:
    current_version = get_installed_version(requirement_name)
    if current_version == "Broken":
        return False

    if requirement_has_version(requirement_name):
        if get_requirement_version(requirement_name) == current_version:
            return True
    if current_version:
        return True
    return False


def requirement_has_version(requirement_name: str) -> bool:
    return get_requirement_version(requirement_name) is not None


def get_requirement_version(requirement_name: str) -> Optional[str]:
    s = requirement_name.split("==")
    if len(s) == 2:
        return s[-1]
    return None


def get_installed_version(
    requirement_name: str, reload: bool = True
) -> Optional[Union[str, version.Version]]:
    import importlib

    if reload:
        importlib.invalidate_caches()
        try:
            if requirement_name in sys.modules:
                importlib.reload(sys.modules[requirement_name])
            else:
                importlib.import_module(requirement_name)
        except (KeyError, ModuleNotFoundError):
            return None
        except Exception as e:
            # print(f'{requirement_name} is broken {e}')
            return "Broken"
            # return None

    try:
        # importlib.reload(sys.modules['pkg_resources'])
        dist = Distribution.from_name(requirement_name)
        if dist:
            return version.parse(dist.version)
    except Exception as e:
        print(e)

    return None


def get_newest_version(requirement_name: str) -> Optional[version.Version]:
    try:
        return version.parse(get_versions_from_index(requirement_name)[-1])
    except HTTPError:
        return None


def get_charset(headers, default: str = "utf-8"):
    # this is annoying.
    try:
        charset = headers.get_content_charset(default)
    except AttributeError:
        # Python 2
        charset = headers.getparam("charset")
        if charset is None:
            ct_header = headers.getheader("Content-Type")
            content_type, params = cgi.parse_header(ct_header)
            charset = params.get("charset", default)
    return charset


def json_get(url: str, headers: Tuple = (("Accept", "application/json"),)) -> str:
    response = urlopen(Request(url=url, headers=dict(headers)))
    code = response.code

    if code != 200:
        err = ConnectionError(f"Unexpected response code {code}")
        err.response_data = response.read()
        raise err

    data = json.loads(response.read().decode(get_charset(response.headers)))
    return data


def get_data_from_index(name: str, index: str = DEFAULT_PIP_INDEX):
    uri = f"{index.rstrip('/')}/{name.split('[')[0]}/json"
    data = json_get(uri)
    return data


def get_versions_from_index(
    name: str, index: str = DEFAULT_PIP_INDEX
) -> Union[None, tuple[Version], Version]:
    try:
        pypi_data = get_data_from_index(name, index)
        releases = pypi_data["releases"]
    except:
        return None

    try:
        return (*sorted(releases, key=version.parse),)
    except InvalidVersion as e:  # VERSION NUMBER MAYBE BROKEN
        print(name, index, e)

        try:
            return [str(version.parse(list(releases.keys())[-1]))]
        except InvalidVersion as e:  # VERSION NUMBER MAYBE BROKEN, GIVE UP
            print(name, index, e)

            return None


def pip_freeze_list() -> List:
    ...


def is_requirement_updatable(requirement_name: str) -> bool:
    if not is_requirement_installed(requirement_name):
        return True

    current_version = get_installed_version(requirement_name)

    if current_version == "Broken":
        return True

    if requirement_has_version(requirement_name):
        if get_requirement_version(requirement_name) != current_version:
            return True

    s = get_newest_version(requirement_name)
    if s:
        if s > current_version:
            return True

    return False


def install_requirements_from_name(
    *requirements_name: Iterable[str],
    upgrade: bool = True,
    ignore_editable_installs: bool = True,
) -> None:
    """
    Install requirements from names.

    :param requirements_name: Name of requirements.
    :param ignore_editable_installs: If an installation is editable do not change
    :param upgrade: Whether to upgrade already installed packages
    """
    # pip.main(["install", "pip", "--upgrade"]) # REQUIRES RESTART OF QGIS

    # if isinstance(requirements_name, Iterable) and len(requirements_name)==1:
    # ... # handle wrong input format
    if ignore_editable_installs:
        try:
            from warg import package_is_editable

            requirements_name = [
                r for r in requirements_name if not package_is_editable(r)
            ]
        except (ImportError, ModuleNotFoundError) as e:
            print(f"missing module, not checking for editable install, {e}")

    # --index-url
    # --upgrade-strategy <upgrade_strategy>
    args = ["install", *requirements_name]
    # args = ["install", "rasterio", "--upgrade"] # RASTERIO for window DOES NOT WORK ATM, should be installed manually

    # TODO: ADD OPTION TO PICK INDEX

    if upgrade:
        args += ["--upgrade"]

    if False:
        import pip

        pip.main(args)
    elif False:
        SP_CALLABLE(["pip"] + args)
    elif True:
        install_pip_if_not_present()

        if is_pip_installed():
            SP_CALLABLE([str(get_qgis_python_interpreter_path()), "-m", "pip", *args])
        else:
            print("PIP IS STILL MISSING!")


def remove_requirements_from_name(*requirements_name: Iterable[str]) -> None:
    """

    Multiple colliding versions may be installed at once, (conda, pip, ....)
    Repeat args let you choose how many times to try to uninstall the packages.
    """
    num_repeat: int = 1
    for _ in range(num_repeat):
        args = ["uninstall", *requirements_name, "-y"]

        if False:
            import pip  # DEPRECATE

            pip.main(args)

        elif False:
            SP_CALLABLE(["pip"] + args)  # Use interpreter path instead

        elif True:
            SP_CALLABLE(
                [str(get_qgis_python_interpreter_path()), "-m", "pip"] + args
            )  # figure out which python!


def is_package_up_to_date(query: str) -> bool:
    return is_requirement_updatable(query)


def is_package_installed(query: str) -> bool:
    return is_requirement_installed(query)


def is_package_updatable(query: str) -> bool:
    return is_requirement_updatable(query)


def is_manual(query: str) -> bool:
    from .. import MANUAL_REQUIREMENTS

    return query in MANUAL_REQUIREMENTS


def append_item_state(query: str) -> str:
    from warg import package_is_editable

    out = query

    if is_manual(query):
        out = f"{out} {InstallStateEnum.manual.value}"

    if get_installed_version(query) == "Broken":
        out = f"{out} {InstallStateEnum.broken.value}"
    elif not is_package_installed(query):
        out = f"{out} {InstallStateEnum.not_installed.value}"

    elif package_is_editable(query):
        out = f"{out} {InstallStateEnum.editable.value}"

    elif is_package_updatable(query):
        out = f"{out} {InstallStateEnum.updatable.value}"

    return out


def strip_item_state(query: str) -> str:
    for state in InstallStateEnum:
        query = query.replace(state.value, "")
    return query.strip()


if __name__ == "__main__":

    def fasga():
        print(is_package_updatable("warg"))

    def gasdsa():
        print(get_versions_from_index("warg"))

    def uhasudh():
        print(get_newest_version("warg"))

    def uhasudasgfagh():
        print(get_versions_from_index("warg"))

    # uhasudasgfagh()

    # uhasudh()

    def ia():
        print(
            get_newest_version("warg"),
            get_installed_version("warg"),
            get_newest_version("warg") == get_installed_version("warg"),
        )

        install_requirements_from_name("that")
        remove_requirements_from_name("that")
