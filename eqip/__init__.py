from .constants import *


def python_version_check(major: int = 3, minor: int = 8):
    """description"""
    import sys

    assert sys.version_info.major == major and sys.version_info.minor >= minor, (
        f"This project is utilises language features only present Python {major}.{minor} and greater. "
        f"You are running {sys.version_info}."
    )


python_version_check()


__version__ = VERSION
__author__ = PLUGIN_AUTHOR
