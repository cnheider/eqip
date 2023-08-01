from pathlib import Path

PROJECT_NAME = "Eqip"
PLUGIN_DIR = Path(__file__).parent.parent
VERSION = "0.0.2"
PLUGIN_AUTHOR = "Heider"

MANUAL_REQUIREMENTS = [
    "qgis"
    # 'qgis' # not visible to pip?
]

try:
    from apppath import AppPath

    PROJECT_APP_PATH = AppPath(PROJECT_NAME, PLUGIN_AUTHOR, VERSION)
except:
    PROJECT_APP_PATH = None

__version__ = VERSION
__author__ = PLUGIN_AUTHOR
