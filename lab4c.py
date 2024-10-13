#!/usr/bin/env python3

# Dictionaries
dict_york = {'Address': '70 The Pond Rd', 'City': 'Toronto', 'Country': 'Canada', 'Postal Code': 'M3J3M6', 'Province': 'ON'}
dict_newnham = {'Address': '1750 Finch Ave E', 'City': 'Toronto', 'Country': 'Canada', 'Postal Code': 'M2J2X5', 'Province': 'ON'}
# Lists
list_keys = ['Address', 'City', 'Country', 'Postal Code', 'Province']
list_values = ['70 The Pond Rd', 'Toronto', 'Canada', 'M3J3M6', 'ON']

def create_dictionary(keys, values):
    # Create a dictionary by pairing keys with values using a while loop
    dictionary = {}
    i = 0
    while i < len(keys) and i < len(values):
        dictionary[keys[i]] = values[i]
        i += 1
    return dictionary

def shared_values(dict1, dict2):
    # Find shared values by using set intersection on values of both dictionaries
    values1 = set(dict1.values())
    values2 = set(dict2.values())
    return values1.intersection(values2)

if __name__ == '__main__':
    # Create dictionary using list_keys and list_values
    york = create_dictionary(list_keys, list_values)
    print('York: ', york)
    
    # Find shared values between dict_york and dict_newnham
    common = shared_values(dict_york, dict_newnham)
    print('Shared Values:', common)
