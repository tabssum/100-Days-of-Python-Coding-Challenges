"""
Find the Largest Number in a List

Problem statement: Given a list of integers, find the largest number without using Python's built-in max() function.

Example:
- Input: [12, 45, 7, 89, 23]
- Output: 89
Concepts: Lists, loops, comparisons
"""

number_lst = list(map(int, input("Enter a list of numbers to find largest number : = ").split()))

print(f"Larges number from list is : {sorted(number_lst)[-1]}")