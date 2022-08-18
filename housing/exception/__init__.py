from email import message
import os
import sys

class HousingExcecption(Exception):
    def __init__(self, error_message : Exception, error_details : sys):
        super().__init__(error_message)
        self.error_message = HousingExcecption.get_detailed_error_message(error_message=error_message,error_details=error_details)
        
    @staticmethod
    def get_detailed_error_message(error_message : Exception, error_details : sys)->str:
        _,_,exec_tb = error_details.exc_info()
        """
        error_message :Exception object
        error_detail : object of sys module
        """
        line_number = exec_tb.tb_frame.f_lineno
        file_name = exec_tb.tb_frame.f_code.co_filename

        error_message = f"Error occured in Script: [{file_name}] at line number : [{line_number}] error message :[{error_message}]"
        return error_message

    def __str__(self):
        return self.error_message

    def __repr__(self) -> str:
        return HousingExcecption.__name__.str()
    

