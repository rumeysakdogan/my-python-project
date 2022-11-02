# List: [] to store multiple elements in a single variable
# A list can contain different data types
# Basic list operations :
# create list
my_list = ["January", "February", "March"]
print(my_list)
#index :      0           1         2

# access items of list
first_element = my_list[0]
print(first_element)

# add an item to list
my_list.append("April")
print(my_list)

# remove item from the list
my_list.remove("March")
print(my_list)

# change items in the list
# if you assign a value to a specific index it will replace the existing one.
my_list[2] = "March"
print(my_list)
