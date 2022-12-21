#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "heider"
__doc__ = r"""

           Created on 12/19/22
           """

import cgi
from pathlib import Path

__all__ = ["install_requirements_from_file", "install_requirements_from_name"]

from typing import Iterable, Tuple


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
        from subprocess import call

        call(["pip"] + args)

    elif True:
        from subprocess import call

        call(["python", "-m", "pip"] + args)


def is_requirement_installed(requirement_name: str) -> bool:
    if requirement_has_version(requirement_name):
        if get_requirement_version(requirement_name) == get_installed_version(
            requirement_name
        ):
            return True
    if get_installed_version(requirement_name):
        return True
    return False


def requirement_has_version(requirement_name: str) -> bool:
    return get_requirement_version(requirement_name) != None


def get_requirement_version(requirement_name: str) -> str:
    s = requirement_name.split("==")
    if len(s) == 2:
        return s[-1]
    return None


def get_installed_version(requirement_name: str, reload: bool = True) -> str:
    import pkg_resources
    import importlib

    try:
        dist = pkg_resources.get_distribution(requirement_name)
        if dist:
            return dist.parsed_version  # .version
    except pkg_resources.DistributionNotFound as e:
        pass
    return None


def get_newest_version(requirement_name: str) -> str:
    from pkg_resources import parse_version
    import os
    import json
    from urllib.request import (
        Request,
        urlopen,
    )  # TODO: should use QgsNetworkAccessManager instead for networking

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
        version_numbers = sorted(data["releases"], key=parse_version)
        return tuple(version_numbers)

    return parse_version(get_versions_pypi(requirement_name)[-1])


def is_requirement_updatable(requirement_name: str) -> bool:
    if not is_requirement_installed(requirement_name):
        return True

    if requirement_has_version(requirement_name):
        if get_requirement_version(requirement_name) != get_installed_version(
            requirement_name
        ):
            return True

    if get_newest_version(requirement_name) > get_installed_version(requirement_name):
        return True

    return False


def install_requirements_from_name(*requirements_name: Iterable[str]) -> None:
    """
    Install requirements from names.

    :param requirements_name: Name of requirements.
    """
    # pip.main(["install", "pip", "--upgrade"]) # REQUIRES RESTART OF QGIS

    # if isinstance(requirements_name, Iterable) and len(requirements_name)==1:
    # ... # handle wrong input format

    args = ["install", *requirements_name, "--upgrade"]
    # args = ["install", "rasterio", "--upgrade"] # RASTERIO for window DOES NOT WORK ATM, should be installed manually

    if False:
        import pip

        pip.main(args)

    elif False:
        from subprocess import call

        call(["pip"] + args)

    elif True:
        from subprocess import call
        import sys

        interpreter = Path(sys.executable)
        call([str(interpreter), "-m", "pip"] + args)


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
            import pip

            pip.main(args)

        elif False:
            from subprocess import call

            call(["pip"] + args)

        elif True:
            from subprocess import call
            import sys

            interpreter = Path(sys.executable)
            call([str(interpreter), "-m", "pip"] + args)  # figure out which python!


if __name__ == "__main__":
    print(
        get_newest_version("warg"),
        get_installed_version("warg"),
        get_newest_version("warg") == get_installed_version("warg"),
    )

    install_requirements_from_name("that")
    remove_requirements_from_name("that")

from .. import MANUAL_REQUIREMENTS


def is_package_up_to_date(query: str) -> bool:
    return is_requirement_updatable(query)


def is_package_installed(query: str) -> bool:
    return is_requirement_installed(query)


def is_package_updatable(query: str) -> bool:
    return is_requirement_updatable(query)


def is_manual(query: str) -> bool:
    return query in MANUAL_REQUIREMENTS


def append_item_state(query: str) -> str:

    if not is_package_installed(query):
        return f"{query} (Not Installed)"

    if is_package_updatable(query):
        return f"{query} (Updatable)"

    if is_manual(query):
        return f"{query} (Manual)"

    return query


def strip_item_state(query: str) -> str:
    return (
        query.replace("(Not Installed)", "")
        .replace("(Updatable)", "")
        .replace("(Manual)", "")
        .strip()
    )


if __name__ == "__main__":

    def _main():
        print(is_package_updatable("warg"))

    _main()
