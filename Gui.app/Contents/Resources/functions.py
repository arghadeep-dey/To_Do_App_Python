from __future__ import annotations

import os
import sys
from pathlib import Path

# Private constants / defaults
APP_NAME = "To_Do_App_Python"
DEFAULT_FILENAME = "todos.txt"


def _default_data_dir() -> Path:
    home = Path.home()
    if sys.platform == "darwin":
        return home / "Library" / "Application Support" / APP_NAME
    if os.name == "nt":
        base = os.environ.get("APPDATA") or os.environ.get("LOCALAPPDATA") or str(home)
        return Path(base) / APP_NAME
    base = os.environ.get("XDG_DATA_HOME") or (home / ".local" / "share")
    return Path(base) / APP_NAME


def _default_todos_path() -> Path:
    override = os.environ.get("TODO_APP_TODOS_FILE")
    if override:
        return Path(override).expanduser()

    # If we're running from inside a macOS .app bundle (e.g. Platypus), do not use the
    # current working directory, as it often points inside the bundle (not writable).
    in_app_bundle = ".app/Contents/" in Path(__file__).as_posix()

    # If a local todos file exists in the current working directory, use it (dev-friendly).
    if not in_app_bundle:
        cwd_file = Path.cwd() / DEFAULT_FILENAME
        if cwd_file.exists():
            return cwd_file

    return _default_data_dir() / DEFAULT_FILENAME


FILEPATH = str(_default_todos_path())

def _ensure_parent_dir(path: Path) -> Path:
    try:
        path.parent.mkdir(parents=True, exist_ok=True)
        return path
    except PermissionError:
        candidates: list[Path] = []

        # 1) Home dir (should be writable for normal users; good persistence)
        candidates.append(Path.home() / f".{APP_NAME}" / DEFAULT_FILENAME)

        # 2) Temp dir (last resort; avoids crashing even in restricted environments)
        tmp_base = os.environ.get("TMPDIR") or "/tmp"
        candidates.append(Path(tmp_base) / APP_NAME / DEFAULT_FILENAME)

        last_err: Exception | None = None
        for candidate in candidates:
            try:
                candidate.parent.mkdir(parents=True, exist_ok=True)
                return candidate
            except Exception as e:  # noqa: BLE001 - deliberate fallback attempts
                last_err = e

        assert last_err is not None
        raise last_err

# Functions for File Management
def get_todos(filepath=FILEPATH):
    """Return a list of all todos from the parameter file"""
    path = Path(filepath)
    path = _ensure_parent_dir(path)
    if not path.exists():
        path.write_text("", encoding="utf-8")
        return []
    return path.read_text(encoding="utf-8").splitlines(keepends=True)

def write_todos(todos_arg,filepath=FILEPATH):
    """Edit the todos file with the parameter file"""
    try:
        path = Path(filepath)
        path = _ensure_parent_dir(path)
        with path.open("w", encoding="utf-8") as file_local:
            file_local.writelines(todos_arg)
        return 1
    except FileNotFoundError:
        print(f"{filepath} does not exist")
        return 0
