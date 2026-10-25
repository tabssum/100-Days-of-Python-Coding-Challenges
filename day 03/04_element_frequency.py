"""
Count the Frequency of Each Element in a List

Problem statement: Write a Python program to count how many times each element appears in a list and store the results in a dictionary.

Example input: [1, 2, 2, 3, 1, 2]

Expected output: {1: 2, 2: 3, 3: 1}

Concepts: lists, dictionaries, loops, counting.
"""

ele_lst = input("Enter a list of numbers to count its frequency : = ").split()

unique_ele = set(ele_lst)

freq_dict = {}
for ele in unique_ele:
    freq_dict[ele] = ele_lst.count(ele)

print(f"Frequency of each element in a list is := {freq_dict}")
