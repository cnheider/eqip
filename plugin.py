# -*- coding: utf-8 -*-
"""
 qpip

                              -------------------
        begin                : 2022-05-23
        git sha              : $Format:%H$
        copyright            : (C) 2022 by Alexandra Institute
        email                : christian.heider@alexandra.dk

"""
import warnings

from qgis.PyQt.QtCore import QCoreApplication, QLocale, QTranslator
from qgis.core import QgsSettings

from .qpip import PLUGIN_DIR, PROJECT_NAME
from .qpip.configuration.options import QPipOptionsPageFactory

# noinspection PyUnresolvedReferences
from .resources import *  # Initialize Qt resources from file resources.py

MENU_INSTANCE_NAME = f"&{PROJECT_NAME.lower()}"
VERBOSE = False


class QPip:
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

        self.options_factory = QPipOptionsPageFactory()

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
