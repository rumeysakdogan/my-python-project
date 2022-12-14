# Looping to execute logic multiple times
# Python has 2 loop commands
# Conditions evaluate to true or false
# are used most commonly in "if statements" and "loops"

# while loop
# execute a set of statements as long as a condition is true.

calculation_of_unit = 24
name_of_unit = "hours"


def days_to_units_with_parameter(num_of_days):
    # condition_check = num_of_days > 0
    return f"{num_of_days} days are {num_of_days * calculation_of_unit} {name_of_unit}"


def validate_and_execute():
    try:
        user_input_number = int(user_input)
        if user_input_number > 0:
            calculated_value = days_to_units_with_parameter(user_input_number)
            print(calculated_value)
        elif user_input_number == 0:
            print("you entered 0, please enter a positive number")
    except ValueError:
        print("you input is not a valid number, please don't ruin my program!")


user_input = ""
while user_input.lower() != "exit":
    user_input = input("Hey user, enter a number of days I will convert it to hours:\n")
    validate_and_execute()

