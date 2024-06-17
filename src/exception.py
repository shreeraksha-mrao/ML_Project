import sys 
import logging
from logger import LOG_FILE_PATH

def error_message_detail(error, error_detail:sys):
   _,_,exc_tb =  error_detail.exc_info()
   file_name = exc_tb.tb_frame.f_code.co_filename
   error_message = "Error occured in python script name[{0}] line number [{1}] error message [{2}]".format(file_name, exc_tb.tb_lineno,str(error) )
   
   return error_message
   
   
class CustomException(Exception):#inherits from base class Exception
    def __init__(self,error_message,error_detail:sys):
        '''
        super().__init__(error_message): Calls the initializer of the base Exception class with the error_message
        '''
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail = error_detail)
        
    def __str__(self):
        return self.error_message

# Example usage
if __name__ == "__main__":
    try:
        a = 1 / 0  # This will raise a ZeroDivisionError
    except Exception as e:
        logging.info("Divivde by zero")
        raise CustomException(e, sys)