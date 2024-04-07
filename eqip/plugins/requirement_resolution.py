import logging
from pathlib import Path

from ..configuration.piper import install_requirements_from_file

__all__ = [
    "get_requirements_file_path",
    "has_requirements_file",
    "install_plugin_requirements",
]


def get_requirements_file_path(
    qgis_plugin: str, requirements_file_name: str = "requirements.txt"
) -> Path:
    """
    Returns the path to the requirements file of the given QGIS plugin with the given name

    :param qgis_plugin:
    :param requirements_file_name:
    :return:
    """
    # plugins_path = PLUGIN_DIR.parent
    from qgis.utils import plugin_paths

    plugins_path = Path(next(iter(plugin_paths)))
    return plugins_path / qgis_plugin / requirements_file_name


def has_requirements_file(qgis_plugin: str) -> bool:
    """
    Checks if the plugin has a requirements file
    :param qgis_plugin:
    :return:
    """
    return get_requirements_file_path(qgis_plugin).exists()


def install_plugin_requirements(plugin_name: str, verbose: bool = False) -> bool:
    """
    Install requirements for a plugin with the given name

    :param plugin_name:
    :param verbose:
    :return:
    """
    if has_requirements_file(plugin_name):
        install_requirements_from_file(get_requirements_file_path(plugin_name))
        return True

    if verbose:
        logging.info(
            f"Did not find any requirements for {plugin_name}",
        )
    return False
