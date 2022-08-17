from setuptools import setup
from typing import List

#Declaring variables for setup functions
PROJECT_NAME = "housing=prediction"
VERSION = "0.0.1"
AUTHOR = "T Raza"
DESCRIPTION = "This is my first ML project"
PACKAGES = ["housing"]
REQUIREMENT_FILE_NAME = "requirements.txt"

def get_requirements_list()->List[str]:     # ->List[str] This will return list in  which there will be string in it.
    """
    Description : This function is going to return list of all the requirements mentioned in requirements.txt file

    return - This function is going to return a list which contain name of libraries mentioned in requirements.txt file.
    """
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        return requirement_file.readlines()


setup(
    name = PROJECT_NAME,
    version= VERSION,
    author= AUTHOR,
    description= DESCRIPTION,
    packages= PACKAGES,
    install_requires = get_requirements_list()
)
