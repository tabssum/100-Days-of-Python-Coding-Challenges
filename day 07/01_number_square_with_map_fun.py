"""
Problem Statement: Use map() to create a new list containing the square of each number.

"""

input_lst=list(map(int,input("Enter a list of numbers to caculate the square of each number: ").split()))


sqaure_list=list(map(lambda x : x*x, input_lst))

print("The square of each number in the list is: ", sqaure_list)
