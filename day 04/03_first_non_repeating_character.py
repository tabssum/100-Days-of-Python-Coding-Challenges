"""
Find the First Non-Repeating Character

Problem statement: Write a Python program to find the first character in a string that appears only once. 
If no such character exists, display an appropriate message.

Example input: "swiss"

Expected output: w

Concepts: Strings, loops, dictionaries, character frequency
"""
str_input = input("Enter a string to find its first Non-Repeating Character := ")


for ch in str_input:
  if str_input.count(ch)==1:
    print(f"First non-repeating character is := {ch}")
    break
else:
  print("No non-repeated character found in the string")
