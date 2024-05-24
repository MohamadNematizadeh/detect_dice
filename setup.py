from setuptools import setup
from pathlib import Path


def pre_install():
    #f = open("README.md" , "r")
    #text = f.read()
    # this_directory = Path(__file__).parent
    # long_description = (this_directory / "README.md").read_text()   
    text =  "# detect dice detect_dice is a simple and fast dice detection library made in Python based on cv2(opencv. This library allows you to perform dice detection operations on images for you"

    return text


setup(name="detect_dice" ,
    version="1.0.4", 
    author="MohammadNematizadeh" , 
    description="This package is in the field of image processing and can perform dice detection for you",
    long_description=pre_install() ,
    requires= [] ,
    author_email="mohammad.nematizzadeh@gmail.com",
    packages=["detect_dice"],
    )
