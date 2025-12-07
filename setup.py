#!/usr/bin/env python

from setuptools import setup, find_packages
import os

setup(
    name="thortils",
    packages=find_packages(where="."),
    package_dir={"": "."},
    version="0.1",
    description="Code related to Ai2-Thor. Try to do one thing once.",
    python_requires=">3.6",
    install_requires=["numpy", "matplotlib", "ai2thor", "open3d", "tqdm"],
    license="MIT",
    author="Kaiyu Zheng",
    author_email="kaiyutony@gmail.com",
)
