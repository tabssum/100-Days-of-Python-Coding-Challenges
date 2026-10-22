"""
Remove Duplicates from a List

Problem statement: Remove duplicate elements from a list while preserving the original order of the remaining elements.

Example:

- Input: [1, 2, 2, 3, 1, 4]
- Output: [1, 2, 3, 4]
Concepts: Lists, sets, iteration

"""

lst_input=list(map(int, input("Enter a list of numbers to remove dumplicates : = ").split()))

final_lst= []
for ele in lst_input:
    if ele not in final_lst:
        final_lst.append(ele)

print(f"List after removing duplicates is : {final_lst}")