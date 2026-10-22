"""
Reverse a String
Problem statement: Write a Python program to reverse a string entered by the user without using a 
built-in reverse function.

Example:
- Input: Python
- Output: nohtyP
"""

str_input = input("Enter a string to reverse it := ")
print(f"Reversed string is := {str_input[::-1]} of original string {str_input}")

