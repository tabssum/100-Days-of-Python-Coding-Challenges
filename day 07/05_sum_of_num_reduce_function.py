"""
Concept / Problem Statement: Use reduce() to find the sum of all numbers in a list.
"""

from functools import reduce

lst1=list(map(int,input("Enter a elements in first list:=").split()))

sum=reduce(lambda x,y: x+y, lst1)

print(f"The sum of all numbers in the given list is: {sum}")


#Concept / Problem Statement: Use reduce() to multiply all numbers in a list.

product=reduce(lambda x,y:x*y, lst1)
print(f"The product of all numbers in the given list is: {product}")
