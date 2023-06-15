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
]

import cgi
import subprocess
import sys
from pathlib import Path
from typing import Iterable, List, Tuple, Optional, Union, Any

import pkg_resources
from pkg_resources.extern.packaging.version import InvalidVersion, Version

# from warg import is_windows # avoid dependency import not standard python pkgs.
CUR_OS = sys.platform
IS_WIN = any(CUR_OS.startswith(i) for i in ["win32", "cygwin"])

SP_CALLABLE = subprocess.check_call  # subprocess.call

# subprocess.Popen(**ADDITIONAL_PIPE_KWS)
# ADDITIONAL_PIPE_KWS =  dict(stderr=subprocess.PIPE,stdout=subprocess.PIPE, stdin=subprocess.PIPE)

if False:  # may no be needed anymore use pkg_resources.safe_version instead
    from warg import passes_kws_to

    @passes_kws_to(pkg_resources.parse_version)
    def catching_parse_version(
        *args, drop_invalid_versions: bool = True, **kwargs
    ) -> Version:
        try:
            return pkg_resources.parse_version(*args, **kwargs)
        except InvalidVersion as e:
            if drop_invalid_versions:
                return Version()
            raise e


def get_qgis_python_interpreter_path() -> Path:
    interpreter_path = Path(sys.executable)
    if IS_WIN:  # For OSGeo4W
        return interpreter_path.parent / "python.exe"

    return interpreter_path


def install_requirements_from_file(requirements_path: Path) -> None:
    """
    Install requirements from a requirements.txt file.

    :param requirements_path: Path to requirements.txt file.

    """

    # pip.main(["install", "pip", "--upgrade"]) # REQUIRES RESTART OF QGIS

    args = ["install", "-r", str(requirements_path), "--upgrade"]
    # args = ["install", "rasterio", "--upgrade"] # RASTERIO for window DOES NOT WORK ATM, should be installed manually

    if False:
        import pip

        pip.main(args)

    elif False:
        SP_CALLABLE(["pip"] + args)

    elif True:
        SP_CALLABLE([str(get_qgis_python_interpreter_path()), "-m", "pip", *args])


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
) -> Optional[Union[str, Version]]:
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
        dist = pkg_resources.get_distribution(requirement_name)
        if dist:
            return dist.parsed_version  # .version
    except pkg_resources.DistributionNotFound as e:
        pass

    return None


def get_newest_version(requirement_name: str) -> Optional[Any]:
    from pkg_resources import parse_version
    import os
    import json
    from urllib.request import (
        Request,
        urlopen,
    )  # TODO: should use QgsNetworkAccessManager instead for networking

    from urllib.error import HTTPError

    try:
        DEFAULT_PIP_INDEX = os.environ.get("PIP_INDEX_URL", "https://pypi.org/pypi/")

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

        def json_get(url: str, headers: Tuple = (("Accept", "application/json"),)):
            request = Request(url=url, headers=dict(headers))
            response = urlopen(request)
            code = response.code
            if code != 200:
                err = ConnectionError(f"Unexpected response code {code}")
                err.response_data = response.read()
                raise err
            raw_data = response.read()
            response_encoding = get_charset(response.headers)
            decoded_data = raw_data.decode(response_encoding)
            data = json.loads(decoded_data)
            return data

        def get_data_pypi(name: str, index: str = DEFAULT_PIP_INDEX):
            uri = f"{index.rstrip('/')}/{name.split('[')[0]}/json"
            data = json_get(uri)
            return data

        def get_versions_pypi(name: str, index: str = DEFAULT_PIP_INDEX):
            data = get_data_pypi(name, index)
            version_numbers = sorted(data["releases"], key=pkg_resources.safe_version)
            return tuple(version_numbers)

        return parse_version(get_versions_pypi(requirement_name)[-1])
    except HTTPError:
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
    *requirements_name: Iterable[str], upgrade: bool = True
) -> None:
    """
    Install requirements from names.

    :param requirements_name: Name of requirements.
    :param upgrade: Whether to upgrade already installed packages
    """
    # pip.main(["install", "pip", "--upgrade"]) # REQUIRES RESTART OF QGIS

    # if isinstance(requirements_name, Iterable) and len(requirements_name)==1:
    # ... # handle wrong input format

    args = ["install", *requirements_name]
    # args = ["install", "rasterio", "--upgrade"] # RASTERIO for window DOES NOT WORK ATM, should be installed manually

    if upgrade:
        args += ["--upgrade"]

    if False:
        import pip

        pip.main(args)
    elif False:
        SP_CALLABLE(["pip"] + args)
    elif True:
        SP_CALLABLE([str(get_qgis_python_interpreter_path()), "-m", "pip", *args])


def remove_requirements_from_name(*requirements_name: Iterable[str]) -> None:
    """

    Multiple colliding versions may be installed at once, (conda, pip, ....)
    Repeat args let you choose how many time to try uninstall the packages.
    """
    num_repeat: int = 1
    for _ in range(num_repeat):
        args = ["uninstall", *requirements_name, "-y"]
        print(args)
        if False:
            import pip  # DEPRECATE

            pip.main(args)

        elif False:
            SP_CALLABLE(["pip"] + args)  # Use interpreter path instead

        elif True:
            interpreter = Path(sys.executable)
            SP_CALLABLE(
                [str(interpreter), "-m", "pip"] + args
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
    out = query

    if is_manual(query):
        out = f"{out} (Manual)"

    if get_installed_version(query) == "Broken":
        out = f"{out} (Broken)"
    elif not is_package_installed(query):
        out = f"{out} (Not Installed)"

    elif is_package_updatable(query):
        out = f"{out} (Updatable)"

    return out


def strip_item_state(query: str) -> str:
    return (
        query.replace("(Not Installed)", "")
        .replace("(Updatable)", "")
        .replace("(Manual)", "")
        .replace("(Broken)", "")
        .strip()
    )


if __name__ == "__main__":

    def _main():
        print(is_package_updatable("warg"))

    _main()

    def ia():
        print(
            get_newest_version("warg"),
            get_installed_version("warg"),
            get_newest_version("warg") == get_installed_version("warg"),
        )

        install_requirements_from_name("that")
        remove_requirements_from_name("that")
