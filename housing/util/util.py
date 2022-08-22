""" util file is not part of pipeline .But there are some functionalities which are actually not part of pipeline
But it is required at multiple places so We will write all the helper functions here like pickling , read yaml etc """


import yaml
from housing.exception import HousingExcecption
import os , sys

def read_yaml_file(file_path:str) ->dict:
    """
    Reads a YAML file and returns the contents as a dictionay.
    file_path:str
    """

    try:

        config_info = None 
        with open(file_path,"rb") as yaml_file:
            return yaml.safe_load(yaml_file)

    except Exception as e:
        raise HousingExcecption(e, sys) from e
        