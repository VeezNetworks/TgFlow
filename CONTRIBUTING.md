# Contributing to TgFlow

Thank you for your interest in contributing to **TgFlow**!

## Development Guidelines

1. **Python Compatibility**: Code must run on Python 3.10, 3.11, 3.12, 3.13, and 3.14.
2. **Type Hints**: All functions and methods must include full PEP 484 type annotations.
3. **Architecture**: Keep modules modular and clean. Respect MTProto 2.0 specifications.
4. **Testing**: Run test suite before submitting pull requests:
   ```bash
   python -m unittest discover tests
   ```
5. **Documentation**: When adding or updating methods, update Sphinx documentation under `docs/` and verify clean build with zero warnings:
   ```bash
   sphinx-build -b html -W docs docs/_build/html
   ```

## Pull Request Process

1. Fork the repository and create your branch from `main`.
2. Ensure all tests pass.
3. Keep commit messages clear, semantic, and descriptive.
4. Submit the pull request with a detailed description of the changes.
