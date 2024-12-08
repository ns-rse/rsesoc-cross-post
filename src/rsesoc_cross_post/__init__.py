"""Initialise the package."""

from importlib.metadata import version

try:
    from ._version import version as __version__
except ImportError:
    __version__ = "unknown version"

release = version("rsesoc_cross_post")
__version__ = ".".join(release.split("."[:2]))
