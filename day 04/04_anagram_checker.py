"""
Check Whether Two Strings Are Anagrams

Problem statement: Write a Python program to check whether two strings contain the same characters with the same frequencies, regardless of their order. Ignore spaces and letter case.

Example input: "Listen", "Silent"

Expected output: The strings are anagrams.

Concepts: Strings, dictionaries, loops, string methods
"""
str1=input("Enter first string:= ").lower()
str2=input("Enter second string:= ").lower()

dict1={}
dict2={}
for ch in str1:
  dict1[ch]=str1.count(ch)

for ch in str2:
  dict2[ch]=str2.count(ch)

res="Anagram" if dict1==dict2 else "Not anagram"
print(res)

