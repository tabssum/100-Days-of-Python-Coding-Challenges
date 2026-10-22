"""
Count the Frequency of Each Character

Problem statement: Write a Python program that counts how many times each character occurs in a string and stores the results in a dictionary. 
Ignore spaces and treat uppercase and lowercase letters as the same.

Example:
- Input: Python
- Output: {'p': 1, 'y': 1, 't': 1, 'h': 1, 'o': 1, 'n': 1}
"""

str_input = input("Enter a string to count the frequency of each character := ").lower()
frequency_dict = {}

for ch in str_input:
    if ch!= " ":
       frequency_dict[ch] = str_input.count(ch)

print(f"Frequency of each character in the string is := {frequency_dict}")