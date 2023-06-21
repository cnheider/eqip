from pathlib import Path


def get_requirements_file_path(qgis_plugin: str) -> Path:
    # plugins_path = PLUGIN_DIR.parent
    from qgis.utils import plugin_paths

    plugins_path = Path(next(iter(plugin_paths)))
    return plugins_path / qgis_plugin / "requirements.txt"


def has_requirements_file(qgis_plugin: str) -> bool:
    return get_requirements_file_path(qgis_plugin).exists()
