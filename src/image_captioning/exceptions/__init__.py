import sys

def error_message_detail(error, error_detail: sys):
    _, _, exc_tb = error_detail.exc_info()
    
    if exc_tb is not None:
        file_name = exc_tb.tb_frame.f_code.co_filename
        line_number = exc_tb.tb_lineno
    else:
        file_name = "Unknown"
        line_number = "Unknown"

    error_message = "Error occured in python script name [{0}] line number [{1}] error message[{2}]".format(
        file_name, line_number, str(error)
    )

    return error_message

class CustomException(Exception):
    def __init__(
        self, 
        error_message, 
        error_detail: sys, 
        status_code: int = 500, 
        response_code: str = "INTERNAL_SERVER_ERROR"
    ):
        # Initialize the base Exception
        super().__init__(error_message)
        
        # 1. Save the HTTP Status Code (e.g., 400, 404, 500)
        self.status_code = status_code
        
        # 2. Save the Custom App Code (e.g., "AUTH_FAILURE", "PROCESSING_FAILED")
        self.response_code = response_code
        
        # 3. Save the SHORT message for the user (e.g., "No emotion detected")
        self.message = str(error_message)
        
        # 4. Save the LONG detailed message for debugging (includes file path/line number)
        self.error_message = error_message_detail(error_message, error_detail=error_detail)

    def __str__(self):
        return self.error_message