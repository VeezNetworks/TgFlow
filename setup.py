from setuptools import setup, find_packages

setup(
    name="pytgflow",
    version="1.8.0",
    description="Pure Python MTProto 2.0 Telegram framework engineered for speed, clean architecture, and modern bot development",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="VeezNetworks",
    author_email="contact@veez.net",
    url="https://github.com/VeezNetworks/TgFlow",
    project_urls={
        "Documentation": "https://tgflow.veez.dev",
        "Repository": "https://github.com/VeezNetworks/TgFlow.git",
        "Issues": "https://github.com/VeezNetworks/TgFlow/issues",
    },
    packages=find_packages(include=["tgflow*"]),
    package_data={
        "tgflow": ["py.typed"],
    },
    include_package_data=True,
    python_requires=">=3.10",
    install_requires=[
        "cryptography>=41.0.0",
    ],
    extras_require={
        "docs": [
            "sphinx>=7.0.0",
            "furo>=2024.1.29",
            "sphinx-copybutton>=0.5.2",
            "sphinx-inline-tabs>=2023.4.21",
        ],
        "test": [
            "pytest>=7.0.0",
            "pytest-asyncio>=0.21.0",
        ],
        "dev": [
            "build",
            "twine",
            "wheel",
            "pytest>=7.0.0",
            "pytest-asyncio>=0.21.0",
            "sphinx>=7.0.0",
            "furo>=2024.1.29",
            "sphinx-copybutton>=0.5.2",
            "sphinx-inline-tabs>=2023.4.21",
        ],
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Programming Language :: Python :: 3.14",
        "Topic :: Communications :: Chat",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
