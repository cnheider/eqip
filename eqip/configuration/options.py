# !/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "heider"
__doc__ = r"""
            TODO: Extract eqip specific code from this file.
           Created on 5/5/22
           """

__all__ = ["EqipOptionsPage", "EqipOptionsPageFactory"]

from importlib import metadata
from itertools import count

# noinspection PyUnresolvedReferences
import qgis

# noinspection PyUnresolvedReferences
from qgis.PyQt import QtGui, uic

# noinspection PyUnresolvedReferences
from qgis.PyQt.QtGui import QStandardItem, QStandardItemModel

# noinspection PyUnresolvedReferences
from qgis.PyQt.QtWidgets import QHBoxLayout, QMessageBox

# noinspection PyUnresolvedReferences
from qgis.core import QgsProject

# noinspection PyUnresolvedReferences
from qgis.gui import QgsOptionsPageWidget, QgsOptionsWidgetFactory

from PyQt5 import QtCore
from PyQt5.QtCore import Qt

from warg import get_requirements_from_file, get_package_location

from .piper import (
    append_item_state,
    install_requirements_from_name,
    is_package_installed,
    remove_requirements_from_name,
    strip_item_state,
)
from .project_settings import DEFAULT_PROJECT_SETTINGS
from .settings import (
    restore_default_project_settings,
    store_project_setting,
    read_project_setting,
)
from .. import MANUAL_REQUIREMENTS, PLUGIN_DIR, PROJECT_NAME, VERSION
from ..plugins import has_requirements_file
from ..plugins.hook import (
    add_plugin_dep_hook,
    remove_plugin_dep_hook,
    is_hook_active,
    HOOK_ART_DISABLED,
    HOOK_ART,
)
from ..utilities import resolve_path, load_icon, get_icon_path

VERBOSE = False

qgis_project = QgsProject.instance()
OptionWidget, OptionWidgetBase = uic.loadUiType(resolve_path("options.ui", __file__))


class EqipOptionsPageFactory(QgsOptionsWidgetFactory):
    def __init__(self):
        super().__init__()

    def icon(self):
        return load_icon("snake_bird.png")

    def createWidget(self, parent):
        return EqipOptionsPage(parent)


class EqipOptionsWidget(OptionWidgetBase, OptionWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.icon_label.setPixmap(QtGui.QPixmap(get_icon_path("snake_bird.png")))
        self.title_label.setText("Eqip")
        self.sponsor_label.setPixmap(QtGui.QPixmap(get_icon_path("pypi.png")))
        self.version_label.setText(f"{VERSION}")

        if VERBOSE:  # TODO: Auto-reload development installs
            from warg import reload_module

            reload_module("jord")
            reload_module("warg")
            reload_module("apppath")
            # reload_requirements(PLUGIN_DIR/requirements.txt)

        from jord.qgis_utilities import reconnect_signal

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
        reconnect_signal(self.refresh_button.clicked, self.populate_plugin_requirements)
        reconnect_signal(
            self.install_requirements_button.clicked, self.on_install_requirement
        )

        if True:  # TODO: Add option for also showing inactive plugins
            if True:
                plugins = qgis.utils.available_plugins
                # plug_ins = qgis.utils.active_plugins
                self.plugin_list = {
                    i: name
                    for i, name in zip(count(), plugins)
                    if has_requirements_file(name)
                }

            elif False:
                self.plugin_list = {
                    i: name
                    for i, (name, obj) in zip(count(), qgis.utils.plugins.items())
                    if has_requirements_file(name)
                }

            self.plugin_selection_combo_box.clear()
            self.plugin_selection_combo_box.addItems([*self.plugin_list.values()])
            self.plugin_selection_combo_box.setCurrentIndex(0)
            self.plugin_selection_combo_box.setEditable(False)
            reconnect_signal(
                self.plugin_selection_combo_box.currentTextChanged,
                self.on_select_plugin,
            )
            if len(self.plugin_list):
                self.selected_plugin = next(iter(self.plugin_list.values()))

            self.populate_plugin_requirements()

        # self.requirements_tree_view.editTriggers.register() # Change text when to append (Pending) until apply has been
        # pressed

        reconnect_signal(
            self.populate_environment_button.clicked, self.on_populate_environment
        )
        reconnect_signal(
            self.update_environment_button.clicked, self.on_update_environment
        )

        reconnect_signal(self.reset_options_button.clicked, self.on_reset_options)

        self.update_status_labels()
        self.hook_asci_art.setAlignment(Qt.AlignCenter)
        # self.environment_list_view.editTriggers.register() # Change text when to append (Pending) until apply has been
        # pressed

    def update_status_labels(self):
        if is_hook_active():
            self.enable_dep_hook_button.setEnabled(False)
            self.disable_dep_hook_button.setEnabled(True)
            self.hook_status_label.setText("Active")
            self.hook_asci_art.setText(HOOK_ART)
        else:
            self.enable_dep_hook_button.setEnabled(True)
            self.disable_dep_hook_button.setEnabled(False)
            self.hook_status_label.setText("Inactive")
            self.hook_asci_art.setText(HOOK_ART_DISABLED)

    def on_reset_options(self):
        restore_default_project_settings()

    def on_select_plugin(self, value):
        self.selected_plugin = value  # self.active_plugins[value]
        self.populate_plugin_requirements()

    def on_auto_enable_changed(self, state):
        store_project_setting("AUTO_ENABLE_DEP_HOOK", state, project_name=PROJECT_NAME)

    def on_enable_hook(self):
        add_plugin_dep_hook()

        self.update_status_labels()

    def on_disable_hook(self):
        remove_plugin_dep_hook()

        self.update_status_labels()

    def on_install_requirement(self):
        pkgs_to_be_installed = []
        pkgs_to_be_removed = []
        for index in range(self.requirements_list_model.rowCount()):
            item = self.requirements_list_model.item(
                index, column=0
            )  # https://doc.qt.io/qtforpython-6/PySide6/QtGui/QStandardItemModel.html#qstandarditemmodel
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

        self.populate_plugin_requirements()  # TODO: change are not necessarily reflected immediately, RESTART REQUIRED FOR NOW!!

    def populate_plugin_requirements(self):
        if hasattr(self, "requirements_list_model"):
            del self.requirements_list_model

        self.requirements_list_model = QStandardItemModel(self.requirements_tree_view)

        for requirement in get_requirements_from_file(
            PLUGIN_DIR.parent / self.selected_plugin / "requirements.txt"
        ):
            name_item = QStandardItem(requirement.name)
            current_version_item = QStandardItem("0")
            state_item = QStandardItem(append_item_state(requirement.name))
            required_version_item = QStandardItem(
                ", ".join([str(s) for s in requirement.specifier])
            )
            extras_item = QStandardItem(f"[{', '.join(requirement.extras)}]")
            location_item = QStandardItem(str(get_package_location(requirement.name)))

            # TODO: ADD Other version of package for installation, by the check-able boxes

            name_item.setCheckable(True)
            if is_package_installed(requirement.name):
                name_item.setCheckState(Qt.Checked)
            else:
                name_item.setCheckState(Qt.Unchecked)

            self.requirements_list_model.appendRow(
                [
                    name_item,
                    current_version_item,
                    state_item,
                    extras_item,
                    required_version_item,
                    location_item,
                ]
            )

        for manual_requirement in MANUAL_REQUIREMENTS:
            # n = f'{append_item_state(r.name)} (Manual)'
            name_item = QStandardItem(manual_requirement)
            current_version_item = QStandardItem("0")
            state_item = QStandardItem(append_item_state(manual_requirement))

            name_item.setCheckable(False)
            if is_package_installed(manual_requirement):
                name_item.setCheckState(Qt.Checked)
            else:
                name_item.setCheckState(Qt.Unchecked)

            self.requirements_list_model.appendRow(
                [name_item, current_version_item, state_item]
            )

        column_headers = [
            "package",
            "current version",
            "state",
            "extras",
            "required version",
            "location",
        ]
        for ci, label in enumerate(column_headers):
            self.requirements_list_model.setHeaderData(
                ci, QtCore.Qt.Horizontal, str(label)
            )

        self.requirements_tree_view.setModel(self.requirements_list_model)

        for ci in range(len(column_headers)):
            self.requirements_tree_view.resizeColumnToContents(ci)

        # TODO: ADD BUTTON TO NOW TO NEXT UNSATISFIED REQUIREMENT
        # requirements_tree_view.scrollTo(item_index)

        self.requirements_tree_view.show()

    def populate_environment(self):
        if hasattr(self, "environment_list_model"):
            del self.environment_list_model

        self.environment_list_model = QStandardItemModel(self.environment_list_view)

        if True:
            for l in [r.name for r in metadata.Distribution().discover()]:
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
        self.populate_plugin_requirements()


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
