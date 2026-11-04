"""
Concept / Problem Statement: Remove empty strings from a list using filter().
"""

lst=list(map(str,input("Enter a list of strings:=").split()))

non_empty_str=list(filter(lambda x:x!="", lst))

print(f"List of non-empty strings from the given list is: {non_empty_str}")
