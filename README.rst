virtualenv
==========

This is based on the `rewrite` branch of virtualenv: https://github.com/pypa/virtualenv/tree/rewrite

What pythons are currently supported in this fork:

* Python 2.6
* PyPy
* PyPy3 (on Windows it doesn't really work cause
  `pip is broken on the 2.4.0 release <https://bitbucket.org/pypy/pypy/issue/1696/can-not-install-pip-with-get-pippy>`_)
* Python 2.6
* Python 2.7
* Python 3.2 (not tested, may work)
* Python 3.3
* Python 3.4

What's currently tested (on Windows |appveyor| and Linux |circleci| |travis|):

* creation
* recreation
* ``--system-site-packages`` (incl. ordering of sites)
* ``.pth`` support
* bin scripts
* tox integration
* C extensions compile properly inside

Debian-flavored linuxes are also supported (with their messy patches on site.py/distutils/sysconfig).

.. |circleci| image:: https://circleci.com/gh/ionelmc/virtualenv/tree/develop.svg?style=svg
    :alt: CircleCI Build Status
    :target: https://circleci.com/gh/ionelmc/virtualenv/tree/develop

.. |travis| image:: http://img.shields.io/travis/ionelmc/virtualenv/develop.png?style=flat
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/ionelmc/virtualenv

.. |appveyor| image:: https://ci.appveyor.com/api/projects/status/github/ionelmc/virtualenv?branch=develop
    :alt: AppVeyor Build Status
    :target: https://ci.appveyor.com/project/ionelmc/virtualenv

What's missing:

* No symlinks or hardlinks, just dumb copies.
* Relocation support (it wasn't really supported in legacy virtualenv anyway).
* You tell me ...

Try it
------

To install this, just ``pip install --ignore-installed https://github.com/ionelmc/virtualenv/archive/develop.zip``.

PyPI package
````````````

There's an alternative package on `PyPI`: `virtualenv-rewrite <https://pypi.python.org/pypi/virtualenv-rewrite/>`_::

    pip install virtualenv-review

.. note::

    If you install it over the legacy virtualenv you may have issues. To keep things simple you should uninstall it
    before, eg::

        pip uninstall virtualenv
        pip install virtualenv-review

Docs
----

For the old documentation, see https://virtualenv.pypa.io/

Changelog
---------

14.1.0 (2015-10-02)
```````````````````

* Update bundled setuptools to ``18.3.2``.
* Update bundled wheel to ``0.26.0``.
* Fixed issues with case normalization on Windows (some paths weren't properly case-normalized).

14.0.0 (2015-09-15)
```````````````````

* Initial PyPI release.