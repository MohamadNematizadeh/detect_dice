from setuptools import setup
from pathlib import Path


def pre_install():
    #f = open("README.md" , "r")
    #text = f.read()
    this_directory = Path(__file__).parent
    long_description = (this_directory / "README.md").read_text()    
    return long_description

with open('./requirements.txt') as f:
    install_requires = f.read().splitlines()


setup(name="detect_dice" ,
    version="1.0.2", 
    author="MohamadNematizadeh" , 
    description="This package is in the field of image processing and can perform dice detection for you",
    long_description=pre_install() ,
    requires= [] ,
    author_email="mohammad.nematizzadeh@gmail.com",
    packages=["detect_dice"] ,
    long_description_content_type='text/markdown' ,
    install_requires= install_requires ,
    url="https://github.com/MohamadNematizadeh/detect_dice" ,
    entry_points={"console_scripts": ["detect_dice=detect_dice.detect_dice:detect_dice"]},
    include_package_data=True
    )
