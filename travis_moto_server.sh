#!/usr/bin/env bash
set -e
pip install flask
python setup.py sdist
pip install dist/moto*.gz
moto_server -H 0.0.0.0 -p 5000
