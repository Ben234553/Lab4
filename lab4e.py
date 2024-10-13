#!/usr/bin/env python3
# Author ID: 123236218

def is_digits(sobj):
    """
    Checks if all characters in the string are digits.

    Args:
        sobj (str): The string to check.

    Returns:
        bool: True if all characters are digits, False otherwise.
    """
    for char in sobj:
        if not char.isdigit():  # Check if the character is not a digit
            return False
    return True  # All characters are digits

if __name__ == '__main__':
    # Test the function with some examples
    test_list = ['x3058', '3058', '8503x', '8503']
    for item in test_list:
        if is_digits(item):
            print(item, 'is an integer.')
        else:
            print(item, 'is not an integer.')
