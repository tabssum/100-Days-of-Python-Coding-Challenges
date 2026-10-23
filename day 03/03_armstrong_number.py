
"""
Check Whether a Number Is an Armstrong Number

Problem statement: Write a Python program to check whether a number is an Armstrong number. A number is an Armstrong number if the sum of each digit raised to the power of the total number of digits equals the original number.

Example input: 153

Expected output: 153 is an Armstrong number

Concepts: digit extraction, loops, exponentiation.
"""
try:
    number = abs(int(input("Enter a number to check if it is an Armstrong number: ")))

    length = len(str(number))

    sum_of_digits = 0
    for d in str(number):
        sum_of_digits += int(d) **length

    print(f"{number} is an Armstrong number" if sum_of_digits == number else f"{number} is not an Armstrong number")
except ValueError:
    print("Invalid input! Please enter a valid integer.")