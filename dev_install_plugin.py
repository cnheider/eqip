from logging import warn
from pathlib import Path

from warg import is_windows

from plugin_config import PROFILE, QGIS_APP_PATH

if is_windows():
    b = QGIS_APP_PATH.user_config
else:
    b = QGIS_APP_PATH.user_data

source_folder = Path(__file__).parent.absolute()
target_folder = b / "profiles" / PROFILE / "python" / "plugins" / source_folder.stem

if False:
    qgis_sys_path = Path(target_folder.anchor) / "OSGeo4W" / "apps" / "qgis" / "python"
    import sys

    sys.path.append(str(qgis_sys_path))
    # C:\OSGeo4W\apps\qgis\python > qgis.pth

# You can also set the environment variable QGIS_PLUGIN_PATH to another place but then all other plugins will be ignored
# QGIS_PLUGINPATH


# QTCREATOR (QT) PLUGINS # https://gis.stackexchange.com/questions/367260/how-to-use-all-qgis-3-custom-widgets-in-qt-designer
"""
The available QGIS Custom Widgets in Qt Designer are defined in QGIS libqgis_customwidgets.

It is easy to find out the library in use.

Go to Qt Designer → Help → About Plugins. You will see the QGIS library in use.
INSTALL PLUGIN
USE PATH "C:\OSGeo4W\apps\qgis\qtplugins\designer\qgis_customwidgets.dll"

ABOVE DOES NOT WORK!!

USE instead
SHORTCUT "Qt Designer with QGIS 3.24.3 custom widgets"
"C:\Program Files\QGIS 3.24.3\bin\bgspawn.exe" "C:\PROGRA~1\QGIS 3.24.3\bin\qgis-designer.bat"

"""

# ''' recompile resources ''' #  ASSUMES PYQT5 is installed
# pyrcc5 resources.qrc -o resources.py

# and make sure that
"""
 <resources>
  <include location="resources.qrc"/>
 </resources>
"""
# is not in the .ui file before loading it in QGIS


if __name__ == "__main__":
    if not target_folder.exists():  # Does it check for casing of filepath in windows?
        try:
            target_folder.symlink_to(source_folder)
        except OSError as e:
            warn(
                "Probably missing privileges to make symlink in target parent folder, try running symlinking as administrator or change write access('may be read only') / owner."
            )
            raise e
        print("symlinked src->target", source_folder, "->", target_folder)
    else:
        print(target_folder, "already exists!")
