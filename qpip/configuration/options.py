# !/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "heider"
__doc__ = r"""
            TODO: Extract qpip specific code from this file.
           Created on 5/5/22
           """

__all__ = ["QPipOptionsPage", "QPipOptionsPageFactory"]

from logging import warning
from typing import Any, Mapping, Optional

import pkg_resources
from PyQt5.QtCore import Qt
from qgis.PyQt import QtGui, uic
from qgis.PyQt.QtGui import QIcon, QStandardItem, QStandardItemModel
from qgis.PyQt.QtWidgets import QHBoxLayout, QMessageBox
from qgis.core import QgsProject
from qgis.gui import QgsOptionsPageWidget, QgsOptionsWidgetFactory

from .piper import (
    append_item_state,
    install_requirements_from_name,
    is_package_installed,
    remove_requirements_from_name,
    strip_item_state,
)
from .project_settings import DEFAULT_PROJECT_SETTINGS
from .. import MANUAL_REQUIREMENTS, PLUGIN_DIR, PROJECT_NAME, VERSION
from ..utilities import resolve_path

qgis_project = QgsProject.instance()


def restore_default_project_settings(
    defaults: Optional[Mapping] = None, *, project_name: str = PROJECT_NAME
):
    if defaults is None:
        defaults = {}
    for key, value in defaults.items():
        store_project_setting(key, value, project_name=project_name)


def store_project_setting(key: str, value: Any, *, project_name: str = PROJECT_NAME):

    if isinstance(value, bool):
        qgis_project.writeEntryBool(project_name, key, value)
    elif isinstance(value, float):
        qgis_project.writeEntryDouble(project_name, key, value)
    # elif isinstance(value, int): # DOES NOT EXIST!
    #    qgis_project.writeEntryNum(project_name, key, value)
    else:
        value = str(value)
        qgis_project.writeEntry(project_name, key, value)

    print(project_name, key, value)


def read_project_setting(
    key: str,
    type_hint: type = None,
    *,
    defaults: Mapping = None,
    project_name: str = PROJECT_NAME,
):
    # read values (returns a tuple with the value, and a status boolean
    # which communicates whether the value retrieved could be converted to
    # its type, in these cases a string, an integer, a double and a boolean
    # respectively)

    if defaults is None:
        defaults = {}

    if type_hint is not None:
        if type_hint is bool:
            val, type_conversion_ok = qgis_project.readBoolEntry(
                project_name, key, defaults.get(key, None)
            )
        elif type_hint is float:
            val, type_conversion_ok = qgis_project.readDoubleEntry(
                project_name, key, defaults.get(key, None)
            )
        elif type_hint is int:
            val, type_conversion_ok = qgis_project.readNumEntry(
                project_name, key, defaults.get(key, None)
            )
        else:
            val, type_conversion_ok = qgis_project.readEntry(
                project_name, key, str(defaults.get(key, None))
            )
    else:
        val, type_conversion_ok = qgis_project.readEntry(
            project_name, key, str(defaults.get(key, None))
        )

    if type_hint is not None:
        val = type_hint(val)

    if False:
        if not type_conversion_ok:
            warning(f"read_plugin_setting: {key} {val} {type_conversion_ok}")

    return val


class QPipOptionsPageFactory(QgsOptionsWidgetFactory):
    def __init__(self):
        super().__init__()

    def icon(self):
        icon_path = read_project_setting(
            "RESOURCES_BASE_PATH",
            defaults=DEFAULT_PROJECT_SETTINGS,
            project_name=PROJECT_NAME,
        )
        return QIcon(f"{icon_path}/icon.png")

    def createWidget(self, parent):
        return QPipOptionsPage(parent)


OptionWidget, OptionWidgetBase = uic.loadUiType(resolve_path("options.ui", __file__))


class QPipOptionsWidget(OptionWidgetBase, OptionWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.icon_label.setPixmap(QtGui.QPixmap(resolve_path("icons/snake_bird.png")))
        self.title_label.setText("qpip")
        self.sponsor_label.setPixmap(QtGui.QPixmap(resolve_path("icons/pypi.png")))
        self.version_label.setText(f"{VERSION}")

        self.refresh_button.clicked.connect(self.populate_requirements)

        self.install_requirements_button.clicked.connect(self.on_install_requirement)
        self.populate_requirements()

        # self.requirements_list_view.editTriggers.register() # Change text when to append (Pending) until apply has been
        # pressed

        self.populate_environment_button.clicked.connect(
            self.on_populate_environment
        )  # May be slow
        self.update_environment_button.clicked.connect(self.on_update_environment)

        # self.environment_list_view.editTriggers.register() # Change text when to append (Pending) until apply has been
        # pressed

    def on_install_requirement(self):
        pkgs_to_be_installed = []
        pkgs_to_be_removed = []
        for index in range(self.requirements_list_model.rowCount()):
            item = self.requirements_list_model.item(index)
            r = strip_item_state(
                item.text()
            )  # TODO: do not rely on text from item but another source for the 'real' requirement query to pip
            if item.isCheckable() and r not in MANUAL_REQUIREMENTS:
                if item.checkState() == Qt.Checked:
                    pkgs_to_be_installed.append(r)
                else:
                    pkgs_to_be_removed.append(r)

        if pkgs_to_be_installed:
            install_requirements_from_name(*pkgs_to_be_installed)

            strc = ",\n".join(pkgs_to_be_installed)
            QMessageBox.information(
                self,
                "qpip",
                f"Updated Python Dependencies:\n{strc}",
            )

        if pkgs_to_be_removed:
            remove_requirements_from_name(*pkgs_to_be_removed)

            strd = ",\n".join(pkgs_to_be_removed)
            QMessageBox.information(
                self,
                "qpip",
                f"Removed Python Dependencies:\n{strd}",
            )

        self.populate_requirements()  # TODO: change are not necessarily reflected immediately, RESTART REQUIRED FOR NOW!!

    def populate_requirements(self):
        if hasattr(self, "requirements_list_model"):
            del self.requirements_list_model

        self.requirements_list_model = QStandardItemModel(self.requirements_list_view)

        with open((PLUGIN_DIR / "qpip" / "requirements.txt")) as f:
            for r in pkg_resources.parse_requirements(f.readlines()):
                item = QStandardItem(append_item_state(r.name))

                item.setCheckable(True)
                if is_package_installed(r.name):
                    item.setCheckState(Qt.Checked)
                else:
                    item.setCheckState(Qt.Unchecked)

                self.requirements_list_model.appendRow(item)

        for r in pkg_resources.parse_requirements(MANUAL_REQUIREMENTS):
            n = append_item_state(r.name)
            # n = f'{append_item_state(r.name)} (Manual)'
            item = QStandardItem(n)

            item.setCheckable(False)
            if is_package_installed(r.name):
                item.setCheckState(Qt.Checked)
            else:
                item.setCheckState(Qt.Unchecked)

            self.requirements_list_model.appendRow(item)

        self.requirements_list_view.setModel(self.requirements_list_model)
        self.requirements_list_view.show()

    def populate_environment(self):
        if hasattr(self, "environment_list_model"):
            del self.environment_list_model

        self.environment_list_model = QStandardItemModel(self.environment_list_view)

        if True:
            for r in pkg_resources.working_set:
                l = r.key
                n = append_item_state(l)

                if len(self.environment_list_model.findItems(n)) < 1:

                    item = QStandardItem(n)
                    item.setCheckable(True)
                    if False:
                        if is_package_installed(l):
                            item.setCheckState(Qt.Checked)
                        else:
                            item.setCheckState(Qt.Unchecked)
                    else:
                        item.setCheckState(Qt.Checked)

                    self.environment_list_model.appendRow(item)

        self.environment_list_view.setModel(self.environment_list_model)
        self.environment_list_view.show()

    def on_update_environment(self):
        ...
        # TODO: STILL NEEDS SOME WORK!
        # self.populate_environment()

    def on_populate_environment(self):
        self.populate_environment()

    def on_refresh_button_clicked(self):
        self.populate_requirements()


class QPipOptionsPage(QgsOptionsPageWidget):
    def __init__(self, parent):
        super().__init__(parent)
        root_layout = QHBoxLayout()
        root_layout.setContentsMargins(0, 0, 0, 0)
        self.options_widget = QPipOptionsWidget()
        root_layout.addWidget(self.options_widget)

        if False:
            root_layout.addWidget(
                QMessageBox(
                    QMessageBox.Information,
                    "qpip",
                    "qpip is a plugin for QGIS that allows you to manage python requirements using pip.\n",
                )
            )

        self.setLayout(root_layout)

    def apply(self):
        pass
