from importlib import import_module
import sys
from flask import Flask
import sys
from housing.logger import logging
from housing.exception import HousingExcecption


app = Flask(__name__)

@app.route("/" , methods = ['GET','POST'])
def index():
    try:
        raise Exception("We are testing custom exception")
    except Exception as e:
        housing = HousingExcecption(e,sys)
        logging.info(housing.error_message)
        logging.info("Testing logging module")
    return "CI CD pipeline has been established"



if __name__ == "__main__" :
    app.run(debug = True)