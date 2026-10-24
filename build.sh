#!/usr/bin/env bash
set -e

echo "==> Cleaning old build artifacts..."
rm -rf build/ dist/ *.egg-info

echo "==> Running test suite..."
python -m unittest discover tests

echo "==> Building distribution packages (wheel and sdist)..."
python -m build

echo "==> Verifying distribution packages with twine..."
twine check dist/*

echo "==> Build completed successfully!"
