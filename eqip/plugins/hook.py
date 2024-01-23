import logging

import pyplugin_installer
import qgis
from qgis.core import QgsProviderRegistry

__all__ = [
    "add_plugin_dep_hook",
    "remove_plugin_dep_hook",
    "is_hook_active",
    "HOOK_ART",
    "HOOK_ART_DISABLED",
]

__doc__ = r"""This assume that pyplugin_installer.instance().processDependencies, exists and get called when a new
plugin is added"""


from .requirement_resolution import install_plugin_requirements

VERBOSE = True
HOOK_ART = """

                    ..
                    #+
                    =#
                    .-
                     =:
                     +:
                     =+
                     :#.
                      #-
            -         =*
            --        :*.
            +%-       :-.
           .*-        :=
            #+       -+.
            .++:...-+=.
               ::::.

"""

HOOK_ART_DISABLED = r"""

         \          ..   /
          \         #+  /
           \        =# /
            \       .-/
             \       /:
              \     /+:
               \   / =+
                \ /  :#.
                 X    #-
            -   / \   =*
            -- /   \  :*.
            +%/     \ :-.
           .*/       \:=
            /+       -\.
           /.++:...-+=.\
          /    ::::.    \

"""


class PluginProcessDependenciesHook:
    """
    # When a new plugin is installed, parse and install requirements from pypi
    """

    def __call__(self, *args, **kwargs) -> None:
        plugin_name = args[0]
        if VERBOSE:
            logging.info(
                self, args, kwargs, f"installing requirements for {plugin_name}"
            )

        install_plugin_requirements(plugin_name, verbose=VERBOSE)


HOOK = None
ORIGINAL_PROCESS_DEP_FUNC = None


def add_plugin_dep_hook() -> PluginProcessDependenciesHook:
    """ """
    global ORIGINAL_PROCESS_DEP_FUNC, HOOK
    try:
        if HOOK is None:
            HOOK = PluginProcessDependenciesHook()
            ORIGINAL_PROCESS_DEP_FUNC = (
                pyplugin_installer.instance().processDependencies
            )

            if VERBOSE:
                print("added plugin hook")
                print(HOOK_ART)

            from warg import pre_decorate

            pyplugin_installer.instance().processDependencies = pre_decorate(
                pyplugin_installer.instance().processDependencies, HOOK
            )
    except ModuleNotFoundError:
        print("warg dependency not found")
        remove_plugin_dep_hook()

    return HOOK


def remove_plugin_dep_hook() -> None:
    global HOOK
    if HOOK is not None:
        if VERBOSE:
            print("removed plugin hook")
            print(HOOK_ART_DISABLED)

        pyplugin_installer.instance().processDependencies = ORIGINAL_PROCESS_DEP_FUNC
        del HOOK
        HOOK = None


def is_hook_active() -> bool:
    return HOOK is not None


if __name__ == "__main__":

    def main():
        print(QgsProviderRegistry.instance().pluginList())
        print(qgis.utils.available_plugins)
        print(qgis.utils.plugin_list)

    def sijas():
        pyplugin_installer.instance().fetchAvailablePlugins(False)
        print(pyplugin_installer.installer_data.plugins.all().keys())

        # MONKEY PATCH PROCRESS OF DEPENDENCIES with call to eqip requirement installer
        # def processDependencies(self, plugin_id):
        from warg import pre_decorate

        pyplugin_installer.instance().processDependencies = pre_decorate(
            pyplugin_installer.instance().processDependencies
        )

        # pyplugin_installer.instance().installPlugin('loadthemall')
        # pyplugin_installer.instance().installFromZipFile('/path/to/plugin/file.zip')
        # pyplugin_installer.instance().uninstallPlugin('loadthemall')

    main()
    sijas()
