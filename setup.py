from setuptools import setup, find_packages
from pathlib import Path
def post_install():
    """ Implement post installation routine """
    with open('./requirements.txt') as f:
        install_requires = f.read().splitlines()

    return install_requires


def pre_install():
    """ Implement pre installation routine """
    # read the contents of your README file
    # global long_description
    # this_directory = Path(__file__).parent
    # long_description = (this_directory / "README.md").read_text() 
    text = "detect_dice is a simple and fast dice detection library made in Python based on cv2(opencv. This library allows you to perform dice detection operations on images for you"
     return text


pre_install()
setup(name="detect_dice" ,
    version="1.0.4", 
    author="MohammadNematizadeh" , 
    description="This package is in the field of image processing and can perform dice detection for you",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',  
    requires= [] ,
    author_email="mohammad.nematizzadeh@gmail.com",
    packages=["detect_dice"],
    )
