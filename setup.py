from setuptools import find_packages, setup
from mlopsdbx import __version__

setup(
    name="mlopsdbx",
    packages=find_packages(exclude=["tests", "tests.*"]),
    setup_requires=["wheel"],
    version=__version__,
    description="mlops on databricks",
    author="mahesh cheetirala",
)
