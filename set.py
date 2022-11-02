# Set: another built-in data type of Python
# as with Lists, used to store multiple items of data
# does not allow DUPLICATE values

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
    list_of_days = user_input.split(", ")
    print(list_of_days)
    print(set(list_of_days))

    print(type(list_of_days))
    print(type(set(list_of_days)))

    for num_of_days_element in set(user_input.split(", ")):
        validate_and_execute()

# Basic Set Operations
# Create a set
my_set = {"january", "february", "march"}

# Access items only via loop!
for element in my_set:
    print(element)

# Add an item to the set
my_set.add("April")
print(my_set)

# Remove an item from the set
my_set.remove("january")
print(my_set)

# Unordered and unchangeable!
# Items in a set do not have a defined order
# Items cannot be referred to by index!
# Items cannot be changed, only added/removed!