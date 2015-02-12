from __future__ import absolute_import, division, print_function

from virtualenv.__about__ import (
    __author__, __copyright__, __email__, __license__, __summary__, __title__,
    __uri__, __version__
)
from virtualenv.core import create


def create_environment(
    home_dir,
    site_packages=False, clear=False,
    unzip_setuptools=False,
    prompt=None, search_dirs=None, never_download=False,
    no_setuptools=False, no_pip=False, symlink=True
):
    create(
        home_dir,
        system_site_packages=site_packages,
        clear=clear,
        prompt=prompt or "",
        extra_search_dirs=search_dirs,
        setuptools=not no_setuptools,
        pip=not no_pip
    )

__all__ = [
    "__title__", "__summary__", "__uri__", "__version__", "__author__",
    "__email__", "__license__", "__copyright__",
    "create",
]
