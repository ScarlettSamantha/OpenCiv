from __future__ import annotations
from setuptools import setup, find_packages
import os
import io


# Function to read requirements.txt
def read_requirements():
    with io.open("requirements.txt") as f:
        return f.read().splitlines()


# Function to read version.py
def read_version():
    version = {}
    with io.open(os.path.join("openciv", "version.py")) as f:
        exec(f.read(), version)
    return version["__version__"]


setup(
    name="openciv",
    version=read_version(),
    author="Scarlett Samantha Verheul",
    author_email="scarlett.verheul@gmail.com",
    description="A opensource civilization game",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/ScarlettSamantha/OpenCiv/",
    packages=find_packages(),
    install_requires=read_requirements(),
    classifiers=[
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "Topic :: Games/Entertainment",
    ],
    python_requires=">=3.12",
)
