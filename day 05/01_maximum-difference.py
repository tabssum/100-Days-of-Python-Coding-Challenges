"""
Find the Maximum Difference
Write a Python program to find the maximum difference between any two elements in a list.

Example:
Input:  [2, 3, 10, 6, 4, 8, 1]
Output: Maximum difference is 8
"""

num_list=list(map(int, input("Enter a list of numbers to find its maximum difference:= ").split()))

if len(num_list) < 2:
    print("Please enter at least two numbers.")
else:
    max_ele=max(num_list)
    min_ele=min(num_list)
    print("Maximum difference is", max_ele-min_ele)