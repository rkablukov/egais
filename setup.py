from setuptools import setup, find_packages
import codecs

with codecs.open("README.md", "r", 'utf_8_sig') as fh:
    long_description = fh.read()

setup(
    name='egais',
    version='1.0',
    author="Roman Kablukov",
    description="Python SDK for Egais",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rkablukov/egais",
    packages=find_packages(include=['egais']),
    include_package_data=True,
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
    install_requires=[
        'lxml'
    ]
)
