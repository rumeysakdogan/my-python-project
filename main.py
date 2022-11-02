from helper import validate_and_execute, user_input_message
# import helper  --> if you import module, you have to access func like helper.function_name
# from helper import *  --> if you import everything from module, you don't need to call func from module name
# import helper as h --> you can use alias to call modules h.function_name
# sample built-in modules
import os
import logging

logger = logging.getLogger("MAIN")
logger.error("Error happened in the app")
print(os.name)

"""user_input = ""
while user_input != "exit":
    user_input = input(user_input_message)  # 20:hours
    days_and_units = user_input.split(":")  # ["20", "hours"]
    days_and_unit_dictionary = {"days": days_and_units[0], "units": days_and_units[1]}
    validate_and_execute(days_and_unit_dictionary)
    # helper.validate_and_execute(days_and_unit_dictionary)"""

