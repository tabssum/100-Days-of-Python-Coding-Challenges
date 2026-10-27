"""

Write a program to group words according to their length using a dictionary.

Example input:
["apple", "bat", "cat", "banana", "dog"]



Expected output:
{    5: ["apple"],    3: ["bat", "cat", "dog"],    6: ["banana"]}



Concepts: loops, dictionaries, len()
"""

input_lst=input("Enter a list of words separated by spaces: ").split()

word_dict = dict()
for word in input_lst:
    length = len(word)
    if length not in word_dict:
        word_dict[length] = []
    word_dict[length].append(word)

print(word_dict)    