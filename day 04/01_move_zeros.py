"""
Move All Zeros to the End of a List

Problem statement: Write a Python program to move all zeros in a list to the end while maintaining the relative order of the non-zero elements.

Example input: [0, 1, 0, 3, 12]

Expected output: [1, 3, 12, 0, 0]

Concepts: Lists, loops, conditions
"""

# Online Python compiler (interpreter)
# Write and run Python online using this editor.



lst_input = list(map(int, input("Enter a list of elements := ").split()))

result=[]

for num in lst_input:
  if num != 0:
    result.append(num)

for i in range(len(lst_input)-len(result)):
  result.append(0)

print(f"List after moving all zeros to the end := {result}")