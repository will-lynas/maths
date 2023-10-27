#!/usr/bin/env bash
set -e
echo "Running pytest"
venv/bin/python -m pytest .
echo "Running mypy"
venv/bin/python -m mypy --strict maths_py
echo "Running pylint"
venv/bin/python -m pylint maths_py
