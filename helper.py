# Modules are used to logically organize your Python code
# Module should contain related code, it is just a .py file
# anything in module is called definitions
# we can use many existing Built-In Python Modules
# e.g. math, random, datetime

def days_to_units_with_parameter(num_of_days, conversion_unit):
    if conversion_unit == "hours":
        return f"{num_of_days} days are {num_of_days * 24} hours"
    elif conversion_unit == "minutes":
        return f"{num_of_days} days are {num_of_days * 24 * 60} minutes"
    elif conversion_unit == "seconds":
        return f"{num_of_days} days are {num_of_days * 24 * 60 * 60} seconds"
    else:
        return "unsupported unit"


def validate_and_execute(days_and_unit_dictionary):
    try:
        user_input_number = int(days_and_unit_dictionary["days"])
        if user_input_number > 0:
            calculated_value = days_to_units_with_parameter(user_input_number, days_and_unit_dictionary["units"])
            print(calculated_value)
        elif user_input_number == 0:
            print("you entered 0, please enter a positive number")
        else:
            print("you input is not a valid number, please don't ruin my program!")
    except ValueError:
        print("you input is not a valid number, please don't ruin my program!")


user_input_message = "Hey user, enter number of days and conversion units:\n"
