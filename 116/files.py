import os
from pathlib import Path

ONE_KB = 1024


def get_files(dirname, size_in_kb):
    """Return files in dirname that are >= size_in_kb"""
    entries = Path(dirname)
    for entry in entries.iterdir():
        if not entry.is_dir() and entry.stat().st_size >= size_in_kb * ONE_KB:
            yield entry
