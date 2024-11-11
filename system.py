import warnings
import inspect
import pandas as pd
import sys
import time
import shutil
import threading

from pathlib import Path
from functools import wraps

from ReMASTER.types import ReMASTERUserWarning

def is_frozen():
    return getattr(sys, 'frozen', False)

def get_root_dir() -> Path:
    if is_frozen():
        # we are running in a bundle
        return Path(sys.executable).parent

    # we are running in a normal Python environment
    return Path(__file__).resolve().parent.parent.parent

def get_data_dir() -> Path:
    return get_root_dir() / 'data'
