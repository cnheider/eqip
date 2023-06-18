# !/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "heider"
__doc__ = r"""
            TODO: Extract eqip specific code from this file.
           Created on 5/5/22
           """

__all__ = ["EqipOptionsPage", "EqipOptionsPageFactory"]

from itertools import count
from logging import warning
from typing import Any, Mapping, Optional

import pkg_resources
import qgis
from PyQt5.QtCore import Qt
from jord.qgis_utilities import reconnect_signal
from qgis.PyQt import QtGui, uic
from qgis.PyQt.QtGui import QIcon, QStandardItem, QStandardItemModel
from qgis.PyQt.QtWidgets import QHBoxLayout, QMessageBox
from qgis.core import QgsProject
from qgis.gui import QgsOptionsPageWidget, QgsOptionsWidgetFactory
from warg import reload_module

from .piper import (
    append_item_state,
    install_requirements_from_name,
    is_package_installed,
    remove_requirements_from_name,
    strip_item_state,
)
from .project_settings import DEFAULT_PROJECT_SETTINGS
from .. import MANUAL_REQUIREMENTS, PLUGIN_DIR, PROJECT_NAME, VERSION
from ..plugins import has_requirements_file
from ..plugins.hook import add_plugin_dep_hook, remove_plugin_dep_hook
from ..utilities import resolve_path

qgis_project = QgsProject.instance()

VERBOSE = False


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


class EqipOptionsPageFactory(QgsOptionsWidgetFactory):
    def __init__(self):
        super().__init__()

    def icon(self):
        icon_path = read_project_setting(
            "RESOURCES_BASE_PATH",
            defaults=DEFAULT_PROJECT_SETTINGS,
            project_name=PROJECT_NAME,
        )
        return QIcon(f"{icon_path}/icons/snake_bird.png")

    def createWidget(self, parent):
        return EqipOptionsPage(parent)


OptionWidget, OptionWidgetBase = uic.loadUiType(resolve_path("options.ui", __file__))


class EqipOptionsWidget(OptionWidgetBase, OptionWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.icon_label.setPixmap(QtGui.QPixmap(resolve_path("icons/snake_bird.png")))
        self.title_label.setText("Eqip")
        self.sponsor_label.setPixmap(QtGui.QPixmap(resolve_path("icons/pypi.png")))
        self.version_label.setText(f"{VERSION}")

        if VERBOSE:  # TODO: Auto-reload development installs
            reload_module("jord")
            reload_module("warg")
            reload_module("apppath")
            # reload_requirements(PLUGIN_DIR/requirements.txt)

        reconnect_signal(self.enable_dep_hook_button.clicked, self.on_enable_hook)
        reconnect_signal(self.disable_dep_hook_button.clicked, self.on_disable_hook)
        s = read_project_setting(  # TODO: Use value below
            "AUTO_ENABLE_DEP_HOOK",
            defaults=DEFAULT_PROJECT_SETTINGS,
            project_name=PROJECT_NAME,
        )
        self.auto_enable_check_box.setCheckState(
            Qt.Checked
        )  # TODO: IMPLEMENT WITH READ_PROJECT_SETTING

        reconnect_signal(
            self.auto_enable_check_box.stateChanged, self.on_auto_enable_changed
        )
        reconnect_signal(self.refresh_button.clicked, self.populate_requirements)
        reconnect_signal(
            self.install_requirements_button.clicked, self.on_install_requirement
        )

        if True:  # TODO: Add option for also showing inactive plugins
            self.active_plugins = {
                i: name
                for i, (name, obj) in zip(count(), qgis.utils.plugins.items())
                if has_requirements_file(name)
            }
            self.plugin_selection_combo_box.clear()
            self.plugin_selection_combo_box.addItems([*self.active_plugins.values()])
            self.plugin_selection_combo_box.setCurrentIndex(0)
            self.plugin_selection_combo_box.setEditable(False)
            reconnect_signal(
                self.plugin_selection_combo_box.currentTextChanged,
                self.on_select_plugin,
            )
            if len(self.active_plugins):
                self.selected_plugin = next(iter(self.active_plugins.values()))

            self.populate_requirements()

        # self.requirements_list_view.editTriggers.register() # Change text when to append (Pending) until apply has been
        # pressed

        reconnect_signal(
            self.populate_environment_button.clicked, self.on_populate_environment
        )
        reconnect_signal(
            self.update_environment_button.clicked, self.on_update_environment
        )

        reconnect_signal(self.reset_options_button.clicked, self.on_reset_options)

        # self.environment_list_view.editTriggers.register() # Change text when to append (Pending) until apply has been
        # pressed

    def on_reset_options(self):
        restore_default_project_settings()

    def on_select_plugin(self, value):
        self.selected_plugin = value  # self.active_plugins[value]
        self.populate_requirements()

    def on_auto_enable_changed(self, state):
        store_project_setting("AUTO_ENABLE_DEP_HOOK", state, project_name=PROJECT_NAME)

    def on_enable_hook(self):
        self.enable_dep_hook_button.setEnabled(False)
        self.disable_dep_hook_button.setEnabled(True)
        add_plugin_dep_hook()

    def on_disable_hook(self):
        self.enable_dep_hook_button.setEnabled(True)
        self.disable_dep_hook_button.setEnabled(False)
        remove_plugin_dep_hook()

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
                "eqip",
                f"Updated Python Dependencies:\n{strc}",
            )

        if pkgs_to_be_removed:
            remove_requirements_from_name(*pkgs_to_be_removed)

            strd = ",\n".join(pkgs_to_be_removed)
            QMessageBox.information(
                self,
                "eqip",
                f"Removed Python Dependencies:\n{strd}",
            )

        self.populate_requirements()  # TODO: change are not necessarily reflected immediately, RESTART REQUIRED FOR NOW!!

    def populate_requirements(self):
        if hasattr(self, "requirements_list_model"):
            del self.requirements_list_model

        self.requirements_list_model = QStandardItemModel(self.requirements_list_view)

        with open((PLUGIN_DIR.parent / self.selected_plugin / "requirements.txt")) as f:
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
        self.populate_environment()  # May be slow

    def on_refresh_button_clicked(self):
        self.populate_requirements()


class EqipOptionsPage(QgsOptionsPageWidget):
    def __init__(self, parent):
        super().__init__(parent)
        root_layout = QHBoxLayout()
        root_layout.setContentsMargins(0, 0, 0, 0)
        self.options_widget = EqipOptionsWidget()
        root_layout.addWidget(self.options_widget)

        if False:
            root_layout.addWidget(
                QMessageBox(
                    QMessageBox.Information,
                    "eqip",
                    "eqip is a plugin for QGIS that allows you to manage python requirements using pip.\n",
                )
            )

        self.setLayout(root_layout)

    def apply(self):
        pass
