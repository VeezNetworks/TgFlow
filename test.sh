#!/usr/bin/env bash
set -e

echo "==> Running TgFlow test suite..."
python -m unittest discover tests -v
