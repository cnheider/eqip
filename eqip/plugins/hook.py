import codecs
import configparser
import os
from pathlib import Path
from typing import Tuple

import qgis

from qgis.core import QgsProviderRegistry
import pyplugin_installer
from warg import pre_decorate


__all__ = ["add_plugin_dep_hook", "remove_plugin_dep_hook", "find_qgis_plugins"]

__doc__ = r"""This assume that pyplugin_installer.instance().processDependencies, exists and get called when a new 
plugin is added"""


class PluginProcessDependenciesHook:
    """
    # When a new plugin is installed, parse and install requirements from pypi
    """

    def __call__(self, *args, **kwargs):
        print("_____________")
        print(self, args, kwargs)
        print("_____________")


HOOK = None
ORIGINAL_PROCESS_DEP_FUNC = None


def add_plugin_dep_hook() -> PluginProcessDependenciesHook:
    """ """
    global ORIGINAL_PROCESS_DEP_FUNC, HOOK
    if HOOK is None:
        HOOK = PluginProcessDependenciesHook()
        ORIGINAL_PROCESS_DEP_FUNC = pyplugin_installer.instance().processDependencies

        print("added plugin hook")

        pyplugin_installer.instance().processDependencies = pre_decorate(
            pyplugin_installer.instance().processDependencies, HOOK
        )
    return HOOK


def remove_plugin_dep_hook() -> None:
    global HOOK
    if HOOK is not None:
        print("removed plugin hook")

        pyplugin_installer.instance().processDependencies = ORIGINAL_PROCESS_DEP_FUNC
        del HOOK
        HOOK = None


def find_qgis_plugins(path: Path) -> Tuple:
    """for internal use: return list of plugins in given path"""
    for plugin in path.glob("*"):
        if plugin.is_dir():
            continue
        if not (plugin / "__init__.py").exists():
            continue

        metadata_file = plugin / "metadata.txt"
        if not metadata_file.exists():
            continue

        cp = configparser.ConfigParser()

        try:
            with codecs.open(str(metadata_file), "r", "utf8") as f:
                cp.read_file(f)
        except:
            cp = None

        plugin_name = os.path.basename(plugin)
        yield (plugin_name, cp)


if __name__ == "__main__":

    def asijdsa():
        from qgis.utils import plugin_paths

        for plugin_path in plugin_paths:
            for plugin_id, parser in find_qgis_plugins(plugin_path):
                if parser is None:
                    continue

    def main():
        print(QgsProviderRegistry.instance().pluginList())
        print(qgis.utils.available_plugins)
        print(qgis.utils.active_plugins)

    def sijas():
        pyplugin_installer.instance().fetchAvailablePlugins(False)
        print(pyplugin_installer.installer_data.plugins.all().keys())

        # MONKEY PATCH PROCRESS OF DEPENDENCIES with call to eqip requirement installer
        # def processDependencies(self, plugin_id):

        pyplugin_installer.instance().processDependencies = pre_decorate(
            pyplugin_installer.instance().processDependencies
        )

        # pyplugin_installer.instance().installPlugin('loadthemall')
        # pyplugin_installer.instance().installFromZipFile('/path/to/plugin/file.zip')
        # pyplugin_installer.instance().uninstallPlugin('loadthemall')

    main()
    sijas()