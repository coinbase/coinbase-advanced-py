#!/usr/bin/env bash
set -eu

tmp=$(mktemp -d)
trap 'rm -rf "$tmp"' EXIT
python setup.py sdist --dist-dir "$tmp"
cp tests/typing/consumer.py "$tmp/"
cd "$tmp"
python -m pip install --no-index --no-deps --no-build-isolation --force-reinstall ./*.tar.gz
python -m mypy --no-incremental --warn-unused-ignores consumer.py
