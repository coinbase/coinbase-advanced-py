import os

from setuptools import find_packages, setup

root = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(root, "requirements.txt"), "r") as fh:
    requirements = fh.readlines()

with open(os.path.join(root, "test_requirements.txt"), "r") as fh:
    test_requirements = fh.readlines()

with open(os.path.join(root, "lint_requirements.txt"), "r") as fh:
    lint_requirements = fh.readlines()

README = open(os.path.join(root, "README.md"), "r").read()

about = {}

with open(os.path.join(root, "coinbase", "__version__.py")) as f:
    exec(f.read(), about)

setup(
    name="coinbase-advanced-py",
    version=about["__version__"],
    license="Apache 2.0",
    description="Coinbase Advanced API Python SDK",
    long_description=README,
    long_description_content_type="text/markdown",
    author="Coinbase",
    url="https://github.com/coinbase/coinbase-advanced-py",
    keywords=["Coinbase", "Advanced Trade", "API", "Advanced API"],
    packages=find_packages(exclude=("tests",)),
    install_requires=[req for req in requirements],
    extras_require={
        "test": [test_req for test_req in test_requirements],
        "lint": [lint_req for lint_req in lint_requirements],
    },
    classifiers=[
        "Intended Audience :: Developers",
        "Intended Audience :: Financial and Insurance Industry",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.8",
)
