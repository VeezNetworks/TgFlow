#!/usr/bin/env bash
set -e

echo "==> Building Sphinx documentation..."
sphinx-build -b html -W docs docs/_build/html
echo "==> Documentation built successfully at docs/_build/html"
