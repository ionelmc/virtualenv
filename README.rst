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
* Python 3.2 (tested but unsupported, check test results for exact situation)
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

Option 1: release from alternate index
``````````````````````````````````````

The alternate index: https://anaconda.org/ionelmc/virtualenv

To install::

    pip install -i https://pypi.anaconda.org/ionelmc/simple virtualenv


Option 2: development version
`````````````````````````````

::

    pip install --ignore-installed https://github.com/ionelmc/virtualenv/archive/develop.zip

Option 3: release with different name
`````````````````````````````````````

There's an alternative package on `PyPI`: `virtualenv-rewrite <https://pypi.python.org/pypi/virtualenv-rewrite/>`_::

    pip install virtualenv-rewrite

.. note::

    If you install it over the legacy virtualenv you may have issues. To keep things simple you should uninstall it
    before, eg::

        pip uninstall virtualenv
        pip install virtualenv-rewrite

Docs
----

For the old documentation, see https://virtualenv.pypa.io/
