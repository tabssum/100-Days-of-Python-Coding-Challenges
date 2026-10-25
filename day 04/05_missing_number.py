"""
Find the Missing Number in a Sequence

Problem statement: A list contains distinct integers from 1 to n, but one number is missing. Write a Python program to find the missing number without using sorting.

Example input: [1, 2, 4, 5, 6], where n = 6

Expected output: Missing number: 3

Concepts: Lists, loops, arithmetic, problem-solving
"""
number_lst=list(map(int,input("Enter a list of numbers to find missing number:= ").split()))

largest=max(number_lst)
smallest=min(number_lst)

for i in range(smallest, largest+1):
  if i not in number_lst:
    print(f"Missing number is : {i}")
    break
else:
    print("No missing number found.")