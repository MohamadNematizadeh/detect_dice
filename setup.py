from setuptools import setup
from pathlib import Path


setup(name="detect_dice" ,
    version="1.0.4", 
    author="MohammadNematizadeh" , 
    description="This package is in the field of image processing and can perform dice detection for you",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    long_description=pre_install() ,
    requires= [] ,
    author_email="mohammad.nematizzadeh@gmail.com",
    packages=["detect_dice"],
    )
