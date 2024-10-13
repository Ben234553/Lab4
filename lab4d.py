#!/usr/bin/env python3
# Strings 1

str1 = 'Hello World!!'
str2 = 'Seneca College'

num1 = 1500
num2 = 150

def first_five(string):
    # Return the first five characters of the string
    return string[:5]

def last_seven(string):
    # Return the last seven characters of the string
    return string[-7:]

def middle_number(number):
    # Convert the number to string and return the second and third characters
    num_str = str(number)
    return num_str[1:3]

def first_three_last_three(str1, str2):
    # Return the first 3 characters of str1 concatenated with the last 3 characters of str2
    return str1[:3] + str2[-3:]

if __name__ == '__main__':
    print(first_five(str1))  # Expected: 'Hello'
    print(first_five(str2))  # Expected: 'Sene'
    
    print(last_seven(str1))  # Expected: 'World!!'
    print(last_seven(str2))  # Expected: 'College'
    
    print(middle_number(num1))  # Expected: '50' (from '1500')
    print(middle_number(num2))  # Expected: '50' (from '150')
    
    print(first_three_last_three(str1, str2))  # Expected: 'Helege' (from 'Hello World!!' + 'Seneca College')
    print(first_three_last_three(str2, str1))  # Expected: 'Sen!!' (from 'Seneca College' + 'Hello World!!')
