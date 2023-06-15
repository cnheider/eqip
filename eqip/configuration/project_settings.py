from .. import PROJECT_NAME
from PyQt5.QtCore import Qt

DEFAULT_PROJECT_SETTINGS = {
    "RESOURCES_BASE_PATH": f":/plugins/{PROJECT_NAME}",
    "AUTO_ENABLE_DEP_HOOK": Qt.Checked,
}
