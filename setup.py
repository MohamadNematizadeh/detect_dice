from pathlib import Path
from setuptools import setup


def post_install():
    text = "#detect_dice is a simple and fast dice detection library made in Python based on cv2(opencv. This library allows you to perform dice detection operations on images for you"

    return text

pre_install()

setup(name="detect_dice" ,
    version="1.0.4", 
    author="MohammadNematizadeh" , 
    description="This package is in the field of image processing and can perform dice detection for you",
    long_description==post_install(),
    requires= [] ,
    author_email="mohammad.nematizzadeh@gmail.com",
    packages=["detect_dice"],
    )
