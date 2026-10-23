"""

Find the Sum of Digits of a Number

Problem statement: Write a Python program to calculate the sum of all digits in a given integer.

Example input: 12345

Expected output: Sum of digits: 15

Concepts: while loop, modulo operator, integer division.

"""

# Approach 1: Using string conversion, a for loop, a list, and Python's built-in sum() function to calculate the sum of digits.
try:
    number = int(input("Enter a number to find its digits sum: = "))
    digit_lst=[]
    for digit in str(number):
        digit_lst.append(int(digit))
    print(f"Sum of digits of a number {number} is := {sum(digit_lst)}")
except ValueError:
    print("Invalid input! Please enter a valid integer.")


# Approach 2: Using a while loop, the modulo operator, and integer division to calculate the sum of digits.
try:
    number=int(input("Enter a number to find its digits sum: = "))
    sum_of_digits=0

    while number>0:
        digit=number%10
        sum_of_digits+=digit
        number=number//10
    print(f"Sum of digits of a number {number} is := {sum_of_digits}")
except ValueError:
    print("Invalid input! Please enter a valid integer.")