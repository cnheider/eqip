#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "Christian Heider Nielsen"
__doc__ = r"""

           Created on 25/03/2020
           """

from pathlib import Path


def test_mac():
    from apppath.utilities.windows_path_utilities import SystemEnum, set_system

    set_system(SystemEnum.mac)

    from apppath import AppPath

    qgis_app = AppPath("QGIS3", "QGIS", roaming=True, normalise_path=False)
    user = Path.home().name

    truth = Path(
        f"/Users/{user}/Library/Application Support/QGIS/QGIS3/profiles/default/python/plugins/qpip"
    )

    default_profile = "default"
    b = qgis_app.user_data

    target_folder = b / "profiles" / default_profile / "python" / "plugins" / "qpip"
    assert (
        truth.absolute() == target_folder.absolute()
    ), f"{truth.absolute(), target_folder.absolute()}"


if __name__ == "__main__":
    test_mac()
