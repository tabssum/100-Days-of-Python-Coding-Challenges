"""
Count Vowels and Consonants

Problem statement: Write a program to count the number of vowels and consonants in a string. 
Ignore spaces, digits, and special characters.

Example:
- Input: Hello World
- Output: Vowels: 3, Consonants: 7
Concepts: Loops, conditions, string methods
"""

str_input = input("Enter a string to calculate the number of vowels and consonants := ")
print(f"Input string is := {str_input}")

cleaned_str = "".join(filter(str.isalpha, str_input)).lower()
print(f"Cleaned string is := {cleaned_str}")

vowels = 0
consonants = 0
for ch in cleaned_str:
    if ch in "aeiou":
        vowels += 1
    else:
        consonants += 1
print(f"Vowels: {vowels}, Consonants: {consonants}")