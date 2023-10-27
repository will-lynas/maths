#!/usr/bin/env bash
set -e
echo "Running pytest"
/usr/bin/env python -m pytest .
echo "Running mypy"
/usr/bin/env python -m mypy --strict maths_py
echo "Running pylint"
/usr/bin/env python -m pylint maths_py
