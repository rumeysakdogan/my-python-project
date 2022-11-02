calculation_to_units = 24
name_of_unit = "hours"
# functions: a block of code which runs only when it is called(executed)
# used to avoid repeating same logic
# a function is defined by using def keyword
def days_to_units():
    print(f"20 days are {20 * calculation_to_units} {name_of_unit}")


days_to_units()


# Parameters(is information can be passed into functions)
# Parameters are also called as arguments

def days_to_units_with_parameter(num_of_days, custom_message):
    print(f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}")
    print(custom_message)


days_to_units_with_parameter(7, "Awesome!")

days_to_units_with_parameter(20)
days_to_units_with_parameter(35)
days_to_units_with_parameter(50)