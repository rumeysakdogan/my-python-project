# For Loop: is used for iterating over a sequence (like a list)
# split() : splits a string into a list e.g. "10 20 15 30" --> [10, 20, 15, 30]
# by default split separates elements with space, but it can be override like this split(",")
# so we can execute something for each item in the list

calculation_of_unit = 24
name_of_unit = "hours"


def days_to_units_with_parameter(num_of_days):
    # condition_check = num_of_days > 0
    return f"{num_of_days} days are {num_of_days * calculation_of_unit} {name_of_unit}"


def validate_and_execute():
    try:
        user_input_number = int(num_of_days_element)
        if user_input_number > 0:
            calculated_value = days_to_units_with_parameter(user_input_number)
            print(calculated_value)
        elif user_input_number == 0:
            print("you entered 0, please enter a positive number")
    except ValueError:
        print("you input is not a valid number, please don't ruin my program!")


user_input = ""
while user_input != "exit":
    user_input = input("Hey user, enter number of days as a comma separated list, and I will convert it to hours:\n")
    for num_of_days_element in user_input.split(", "):
        validate_and_execute()
