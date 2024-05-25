from pathlib import Path
from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()


setup(name="detect_dice" ,
    version="1.0.11", 
    author="MohammadNematizadeh" ,
    author_email="mohammad.nematizzadeh@gmail.com",
    description="This package is in the field of image processing and can perform dice detection for you",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MohamadNematizadeh/detect_dice",
    requires= [] ,
    packages=["detect_dice"])
