import codecs
import configparser
import os
from pathlib import Path

import qgis

from qgis import QgsProviderRegistry


class PluginTracker:
    ...


PLUGIN_TRACKER = PluginTracker()


# When a new plugin is installed, parse and install requirements from pypi


def add_tracker():
    PLUGIN_TRACKER


def remove_tracker():
    PLUGIN_TRACKER


def asijdsa():
    from qgis.utils import plugin_paths

    for pluginpath in plugin_paths:
        for plugin_id, parser in findPlugins(pluginpath):
            if parser is None:
                continue


def findPlugins(path: Path):
    """for internal use: return list of plugins in given path"""
    for plugin in path.glob("*"):
        if plugin.is_dir():
            continue
        if not (plugin / "__init__.py").exists():
            continue

        metadataFile = plugin / "metadata.txt"
        if not metadataFile.exists():
            continue

        cp = configparser.ConfigParser()

        try:
            with codecs.open(str(metadataFile), "r", "utf8") as f:
                cp.read_file(f)
        except:
            cp = None

        pluginName = os.path.basename(plugin)
        yield (pluginName, cp)


if __name__ == "__main__":

    def main():
        print(QgsProviderRegistry.instance().pluginList())
        print(qgis.utils.available_plugins)
        print(qgis.utils.active_plugins)

    def sijas():
        import pyplugin_installer

        pyplugin_installer.instance().fetchAvailablePlugins(False)
        print(pyplugin_installer.installer_data.plugins.all().keys())

        # MONKEY PATCH PROCRESS OF DEPENDENCIES with call to eqip requirement installer
        # def processDependencies(self, plugin_id):
        def processDependencies_decorator(method):
            def decorate_processDependencies(self=None):
                print("decorated")

                return method(self)

            return decorate_processDependencies

        pyplugin_installer.processDependencies = processDependencies_decorator(
            pyplugin_installer.processDependencies
        )

        # pyplugin_installer.instance().installPlugin('loadthemall')
        # pyplugin_installer.instance().installFromZipFile('/path/to/plugin/file.zip')
        # pyplugin_installer.instance().uninstallPlugin('loadthemall')

    sijas()
