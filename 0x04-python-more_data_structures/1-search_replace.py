#!/usr/bin/python3
def search_replace(my_list, search, replace):
# Create a new list to store the modified elements
    new_list = []

# Iterate through the elements in the original list
    for item in my_list:
# Check if the current element is equal to the 'search' element
# If it is, replace it with the 'replace' element; otherwise, keep it unchanged
        if item == search:
            new_list.append(replace)
        else:
            new_list.append(item)

       return new_list
