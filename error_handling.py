# Try/Except
# the try block: lets you "test" a block of code for errors
# the except block: catches the error and lets you handle it


calculation_of_unit = 24
name_of_unit = "hours"


def days_to_units_with_parameter(num_of_days):
    return f"{num_of_days} days are {num_of_days * calculation_of_unit} {name_of_unit}"


def validate_and_execute():
    try:
        user_input_number = int(user_input)
        if user_input_number > 0:
            calculated_value = days_to_units_with_parameter(user_input_number)
            print(calculated_value)
        elif user_input_number == 0:
            print("you entered 0, please enter a positive number")
        else:
            print("you entered a negative number, no conversion for you!")
    except ValueError:
        print("you input is not a valid number, please don't ruin my program!")


user_input = input("Hey user, enter a number of days I will convert it to hours:\n")
validate_and_execute()