# Dictionary: are used to store values in key:value pairs
# Is a collection, which does not allow duplicate values
# my_dict = { "days": 20, "units": "hours"}
# we can access values in dictionary by using key names
# my_dict["days"] = 20 , my_dict["units"] = hours


def days_to_units_with_parameter(num_of_days, conversion_unit):
    if conversion_unit == "hours":
        return f"{num_of_days} days are {num_of_days * 24} hours"
    elif conversion_unit == "minutes":
        return f"{num_of_days} days are {num_of_days * 24 * 60} minutes"
    elif conversion_unit == "seconds":
        return f"{num_of_days} days are {num_of_days * 24 * 60 * 60} seconds"
    else:
        return "unsupported unit"


def validate_and_execute():
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


user_input = ""
while user_input != "exit":
    user_input = input("Hey user, enter number of days and conversion units:\n")  # 20:hours
    days_and_units = user_input.split(":")  # ["20", "hours"]
    print(days_and_units)
    days_and_unit_dictionary = {"days": days_and_units[0], "units": days_and_units[1]}
    print(days_and_unit_dictionary)
    validate_and_execute()