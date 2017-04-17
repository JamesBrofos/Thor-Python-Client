import os
from setuptools import setup, find_packages, Command


# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


class CleanCommand(Command):
    """Custom clean command to tidy up the project root."""
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        os.system("rm -vrf ./build ./dist ./*.pyc ./*.egg-info")


setup(
    name="thor_client",
    version="1.0",
    author="James Brofos",
    author_email="james@brofos.org",
    description="Client-side Bayesian optimization infrastructure in Python.",
    license="Copyright (c) James Brofos 2017",
    packages=find_packages(exclude="tests"),
    long_description=read("README.md"),
    install_requires=[],
    cmdclass={
        "clean": CleanCommand,
    }
)
