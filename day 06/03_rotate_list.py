"""
Rotate a list to the left by K positions

Input: List [1, 2, 3, 4, 5], K = 2

Expected output: [3, 4, 5, 1, 2]
"""

# Online Python compiler (interpreter)
# Write and run Python online using this editor.

number_list=list(map(int, input("Enter a list of numbers:= ").split()))

k= int(input("Enter number of rotations:= "))

rotated_list=[]
for i in range(k,len(number_list)):
  rotated_list.append(number_list[i])

for i in range(0,k):
  rotated_list.append(number_list[i])

print(f"Original list : {number_list}")

print(f"list  after {k} rotations is: {rotated_list}")