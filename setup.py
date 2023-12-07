import os

from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), "requirements.txt"), "r") as fh:
    requirements = fh.readlines()

about = {}

root = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(root, "coinbase", "__version__.py")) as f:
    exec(f.read(), about)

setup(
    name="coinbase-advanced-py",
    version=about["__version__"],
    AUTHOR="Coinbase",
    packages=find_packages(),
    install_requires=[req for req in requirements],
    python_requires=">=3.8",
)
