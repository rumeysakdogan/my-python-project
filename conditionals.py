# Conditionals
# Expressions that evaluate to either true or false
# Equals: a == b
# Not Equals: a != b
# Less than: a < b
# Less than or equal to: a <= b
# Greater than: a > b
# Greater than or equal to: a >= b

calculation_of_unit = 24
name_of_unit = "hours"


def days_to_units_with_parameter(num_of_days):
    # condition_check = num_of_days > 0
    return f"{num_of_days} days are {num_of_days * calculation_of_unit} {name_of_unit}"


def validate_and_execute():
    if user_input.isdigit():
        user_input_number = int(user_input)
        if user_input_number > 0:
            calculated_value = days_to_units_with_parameter(user_input_number)
            print(calculated_value)
        elif user_input_number == 0:
            print("you entered 0, please enter a positive number")
    else:
        print("you input is not a valid number, please don't ruin my program!")


user_input = input("Hey user, enter a number of days I will convert it to hours:\n")
validate_and_execute()





