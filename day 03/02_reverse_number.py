"""
Reverse a Number

Problem statement: Write a Python program to reverse the digits of a given integer without converting it into a string.

Example input: 1234

Expected output: Reversed number: 4321

Concepts: while loop, modulo operator, integer division.
"""

#Approach 1: Using string slicing to reverse the digits of a number.
try:
    number = int(input("Enter a number to reverse it : = "))
    reverse_number = str(number)[::-1]
    print(f"Reversed number of a number {number} is := {reverse_number}")
except ValueError:
    print("Invalid input! Please enter a valid integer.")

#Approach 2: Using a while loop, the modulo operator, and integer division to reverse the digits of a number.
try:
    number=int(input("Enter a number to reverse it:= "))
    reversed_number=0
    while number>0:
        digit=number%10
        reversed_number=reversed_number*10+digit
        number=number//10
    print(f"Reversed number of a number {number} is := {reversed_number}")
except ValueError:
    print("Invalid input! Please enter a valid integer.")
