# to ask the user for an input, built-in function
# Python stops executing when it comes to the input()
# input() always returns a string
user_input = int(input("Hey user, enter a number of days I will convert it to hours:\n"))

calculation_of_unit = 24
name_of_unit = "hours"


def days_to_units_with_parameter(num_of_days):
    return f"{num_of_days} days are {num_of_days * calculation_of_unit} {name_of_unit}"
    # return values: a function can return data as a result


calculated_value = days_to_units_with_parameter(user_input)
print(calculated_value)