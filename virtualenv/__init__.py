from __future__ import absolute_import, division, print_function

from virtualenv.__about__ import (
    __author__, __copyright__, __email__, __license__, __summary__, __title__,
    __uri__, __version__
)

# some support for old api in legacy virtualenv
from virtualenv.core import create
from virtualenv.__main__ import main  # flake8: noqa


__all__ = [
    "__title__", "__summary__", "__uri__", "__version__", "__author__",
    "__email__", "__license__", "__copyright__",
    "create", "create_environment", "main",
]

def create_environment(
    home_dir,
    site_packages=False, clear=False,
    unzip_setuptools=False,
    prompt=None, search_dirs=None, never_download=False,
    no_setuptools=False, no_pip=False, symlink=True
):  # flake8: noqa
    create(
        home_dir,
        system_site_packages=site_packages,
        clear=clear,
        prompt=prompt or "",
        extra_search_dirs=search_dirs,
        setuptools=not no_setuptools,
        pip=not no_pip
    )
