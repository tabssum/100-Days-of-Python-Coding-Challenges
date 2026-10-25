"""
Find the Second-Largest Unique Number in a List

Problem statement: Write a Python program to find the second-largest distinct number in a list without 
using sort() or sorted(). Handle cases where fewer than two distinct numbers exist.

Example input: [10, 5, 8, 10, 7]

Expected output: Second-largest number: 8

Concepts: lists, comparisons, loops, edge cases.
"""

lst_input = list(map(int, input("Enter elements list to find second largest number : = ").split()))

unique_ele=list(set(lst_input))

if len(unique_ele) < 2:
    print("There are fewer than two distinct numbers in the list.")
else:
    lar = max(unique_ele)

    unique_ele.remove(lar)

    second_largest = max(unique_ele)

    print(f"Second-largest number: {second_largest}")