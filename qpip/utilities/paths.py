import os
from pathlib import Path

__all__ = ["resolve_path"]


def resolve_path(path: str, base_path: Path = None) -> str:
    if not base_path:
        base_path = Path(os.path.realpath(__file__)).parent.parent.parent
    base_path = Path(base_path)
    if base_path.is_file():
        base_path = base_path.parent
    return str(base_path / path)
