#!/bin/bash -eEx

git merge develop
bumpversion minor
rm -rf dist build *.egg-info 
python setup.py clean --all sdist bdist_wheel
twine upload dist/*

DIST=virtualenv python setup.py clean --all sdist bdist_wheel
binstar upload dist/*
