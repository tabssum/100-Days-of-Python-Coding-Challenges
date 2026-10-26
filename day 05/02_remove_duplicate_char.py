"""
Remove Duplicate Characters
Write a Python program to remove duplicate characters from a string while preserving the original order.
"""

str_input=input("Enter a string to remove duplicate characters from it:=")

unique_char=[]
for ch in str_input:
  if ch not in unique_char:
    unique_char.append(ch)
    
unique_str = "".join(unique_char) 
print(f"String after removing duplicates char is:= {unique_str}")