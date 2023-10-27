#!/usr/bin/env bash
set -e
echo "Running pytest"
/usr/bin/env python -m pytest . --no-header
echo "Pytest passed"

printf %"$COLUMNS"s |tr " " "-"
echo "Running mypy"
/usr/bin/env python -m mypy --strict maths_py
echo "Mypy passed"

printf %"$COLUMNS"s |tr " " "-"
echo "Running pylint"
/usr/bin/env python -m pylint maths_py tests
echo "Pylint passed"
