#We create setup.py whenever we deploy this project as a library.i.e we wanted to create 
#library just like sklearn etc

from setuptools import setup, find_packages
from typing import List

#Declaring variables for setup functions
PROJECT_NAME = "housing=prediction"
VERSION = "0.0.3"
AUTHOR = "T Raza"
DESCRIPTION = "This is my first ML project"
PACKAGES = find_packages  # This find_packages is going to seach for our own code, all the folders wherever it will find __init__, those folder names it is going to return and then it will try to isnstall.
REQUIREMENT_FILE_NAME = "requirements.txt"

def get_requirements_list()->List[str]:     # ->List[str] This will return list in  which there will be string in it.
    """
    Description : This function is going to return list of all the requirements mentioned in requirements.txt file

    return - This function is going to return a list which contain name of libraries mentioned in requirements.txt file.
    """
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        return requirement_file.readlines().remove("-e .") # .remove("-e .") has been used here because already find_packages has bee used here which does the same work.



setup(
    name = PROJECT_NAME,
    version= VERSION,
    author= AUTHOR,
    description= DESCRIPTION,
    packages= PACKAGES,
    install_requires = get_requirements_list()
)
