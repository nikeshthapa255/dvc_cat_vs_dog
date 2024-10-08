import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from catvsdog_model.config.core import PACKAGE_ROOT, config
with open(PACKAGE_ROOT / "VERSION") as version_file:
    __version__ = version_file.read().strip()