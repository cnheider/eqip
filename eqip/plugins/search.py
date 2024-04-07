import codecs
import configparser
import logging
import os
from pathlib import Path
from typing import Tuple

__all__ = ["find_qgis_plugins"]


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

        config_parser = configparser.ConfigParser()

        try:
            with codecs.open(str(metadata_file), "r", "utf8") as f:
                config_parser.read_file(f)
        except Exception as e:
            config_parser = None
            logging.error(e)

        yield (os.path.basename(plugin), config_parser)  # plugin_name


if __name__ == "__main__":

    def asijdsa():
        from qgis.utils import plugin_paths

        for plugin_path in plugin_paths:
            for plugin_id, parser in find_qgis_plugins(plugin_path):
                if parser is None:
                    continue
