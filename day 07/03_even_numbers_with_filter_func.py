"""
Problem Statement: Use filter() to select only even numbers from a list.
"""

lst=list(map(int, input("Enter a list of numbers:=").split()))


even=list(filter(lambda x: x%2==0, lst1))

print(f"List of even numbers from the given list is: {even}")