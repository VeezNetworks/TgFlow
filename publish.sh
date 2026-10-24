#!/usr/bin/env bash
set -e

if [ -z "$PYPI_API_TOKEN" ]; then
    echo "Error: PYPI_API_TOKEN environment variable is not set."
    echo "Usage: PYPI_API_TOKEN=pypi-... ./publish.sh"
    exit 1
fi

echo "==> Cleaning previous builds..."
rm -rf build/ dist/ *.egg-info

echo "==> Building fresh packages..."
python -m build

echo "==> Verifying packages with twine..."
twine check dist/*

echo "==> Uploading to PyPI..."
twine upload -u __token__ -p "$PYPI_API_TOKEN" dist/*

echo "==> Successfully published to PyPI!"
