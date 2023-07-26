from PyQt5.QtCore import Qt

from .. import PROJECT_NAME

DEFAULT_PROJECT_SETTINGS = {
    "RESOURCES_BASE_PATH": f":/{PROJECT_NAME.lower()}",
    "AUTO_ENABLE_DEP_HOOK": Qt.Checked,
}
