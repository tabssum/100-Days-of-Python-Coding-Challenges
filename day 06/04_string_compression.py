"""
Compress a string by counting consecutive characters

Input: "aaabbccccdaa"

Expected output: "a3b2c4d1a2"
"""

from itertools import groupby

s = input("Enter a string: ")

result = ""

for char, group in groupby(s):
    count = len(list(group))
    result += char + str(count)

print("Compressed string:", result)