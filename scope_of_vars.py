# A variable is only available from inside the region it is created
# Global scope = variables available from within any source
# Local scope = variables created inside function, can only be used inside that function
calculation_to_units = 24
name_of_unit = "hours"


def days_to_units_with_parameter(num_of_days, custom_message):
    print(f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}")
    print(custom_message)


def scope_check(num_of_days):
    my_var = "variable inside function"
    print(name_of_unit)  # global variable
    print(num_of_days)   # local variable
    print(my_var)


scope_check(15)
