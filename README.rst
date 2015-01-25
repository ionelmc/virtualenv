virtualenv
==========

This is based on the `rewrite` branch of virtualenv: https://github.com/pypa/virtualenv/tree/rewrite

What pythons are currently supported in this fork:

* Python 2.6
* PyPy
* PyPy3
* Python 2.6
* Python 2.7
* Python 3.2
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

* no symlinks or hardlinks, just dumb copies
* relocation support
* you tell me ...

For the old documentation, see https://virtualenv.pypa.io/
