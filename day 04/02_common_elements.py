"""
Find Common Elements in Two Lists

Problem statement: Write a Python program to find the elements that appear in both lists. Return each common element only once.

Example input: list1 = [1, 2, 3, 4], list2 = [3, 4, 5, 6]

Expected output: [3, 4]

Concepts: Lists, sets, membership operators
"""
lst_input_1 = list(map(int, input("Enter a list of elements := ").split()))
lst_input_2 = list(map(int, input("Enter a list of elements := ").split()))

result=[]

result=list(set(lst_input_1).intersection(set(lst_input_2)))

print(f"Common elements: {result}")