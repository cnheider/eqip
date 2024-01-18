"""DockWidget test.

.. note:: This program is free software; you can redistribute it and/or modify
     it under the terms of the GNU General Public License as published by
     the Free Software Foundation; either version 2 of the License, or
     (at your option) any later version.

"""

__author__ = "asga@aosdsd.ds"
__date__ = "2022-05-24"
__copyright__ = "Copyright 2022, asd"

import unittest

from ...eqip.widgets.dock_widget import EqipDockWidget
from ..utilities import get_qgis_app

QGIS_APP = get_qgis_app()


class EqipDockWidgetTest(unittest.TestCase):
    """Test dockwidget works."""

    def setUp(self):
        """Runs before each test."""
        self.dockwidget = EqipDockWidget(None)

    def tearDown(self):
        """Runs after each test."""
        self.dockwidget = None

    def test_dockwidget_ok(self):
        """Test we can click OK."""
        pass


if __name__ == "__main__":
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(EqipDockWidgetTest)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
