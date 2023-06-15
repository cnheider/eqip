# -*- coding: utf-8 -*-
"""
 eqip

                              -------------------
        begin                : 2022-05-23
        git sha              : $Format:%H$
        copyright            : (C) 2022 by Alexandra Institute
        email                : christian.heider@alexandra.dk

"""
import warnings

import pkg_resources
from qgis.PyQt.QtCore import QCoreApplication, QLocale, QTranslator
from qgis.core import QgsSettings

# noinspection PyUnresolvedReferences
from .resources import *  # Initialize Qt resources from file resources.py

from .eqip import PLUGIN_DIR, PROJECT_NAME
from .eqip.configuration.options import EqipOptionsPageFactory, read_project_setting
from .eqip.configuration.piper import install_requirements_from_name
from .eqip.configuration.project_settings import DEFAULT_PROJECT_SETTINGS

# from .eqip.plugins.hook import add_plugin_dep_hook


MENU_INSTANCE_NAME = f"&{PROJECT_NAME.lower()}"
VERBOSE = False


class Eqip:
    """QGIS Plugin Implementation."""

    def __init__(self, iface):
        """Constructor.

        :param iface: An interface instance that will be passed to this class
            which provides the hook by which you can manipulate the QGIS
            application at run time.
        :type iface: QgsInterface
        """

        self.iface = iface  # Save reference to the QGIS interface

        self.plugin_dir = PLUGIN_DIR

        locale = QgsSettings().value(
            f"{PROJECT_NAME}/locale/userLocale", QLocale().name()
        )

        if isinstance(locale, str):
            locale = locale[0:2]  # locale == "en"
            locale_path = self.plugin_dir / "i18n" / f"{PROJECT_NAME}_{locale}.qm"

            if locale_path.exists():
                self.translator = QTranslator()
                self.translator.load(str(locale_path))
                QCoreApplication.installTranslator(self.translator)
        else:
            warnings.warn(
                f"Unable to determine locale for {PROJECT_NAME} was {type(locale)} {locale}"
            )

        self.menu = self.tr(MENU_INSTANCE_NAME)

        self.options_factory = EqipOptionsPageFactory()

        if False:
            with open((PLUGIN_DIR / "eqip" / "requirements.txt")) as f:
                install_requirements_from_name(
                    *[
                        r.project_name
                        for r in pkg_resources.parse_requirements(f.readlines())
                    ]
                )

            if read_project_setting(
                "AUTO_ENABLE_DEP_HOOK",
                defaults=DEFAULT_PROJECT_SETTINGS,
                project_name=PROJECT_NAME,
            ):
                ...
                # add_plugin_dep_hook()

        # Check if plugin was started the first time in current QGIS session
        # Must be set in initGui() to survive plugin reloads
        # self.first_start = None

    # noinspection PyMethodMayBeStatic
    def tr(self, message):
        """Get the translation for a string using Qt translation API.

        We implement this ourselves since we do not inherit QObject.

        :param message: String for translation.
        :type message: str, QString

        :returns: Translated version of message.
        :rtype: QString
        """
        # noinspection PyTypeChecker,PyArgumentList,PyCallByClass
        return QCoreApplication.translate(PROJECT_NAME, message)

    def initGui(self):
        self.options_factory.setTitle(self.tr(PROJECT_NAME))
        self.iface.registerOptionsWidgetFactory(self.options_factory)

    def unload(self):
        self.iface.unregisterOptionsWidgetFactory(self.options_factory)
        del self.options_factory
