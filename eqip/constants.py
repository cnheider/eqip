from pathlib import Path

from apppath import AppPath

PROJECT_NAME = "Eqip"
PLUGIN_DIR = Path(__file__).parent.parent
VERSION = "0.0.1"
PLUGIN_AUTHOR = "Heider"
PROJECT_APP_PATH = AppPath(PROJECT_NAME, PLUGIN_AUTHOR, VERSION)
MANUAL_REQUIREMENTS = [
    "qgis"
    # 'qgis' # not visible to pip?
]

__version__ = VERSION
__author__ = PLUGIN_AUTHOR
