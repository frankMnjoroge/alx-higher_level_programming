def simple_delete(a_dictionary, key=""):
    # Check if the key is present in the dictionary
    if key in a_dictionary:
        # If the key exists, delete it from the dictionary
        del a_dictionary[key]
        return a_dictionary
