str_input=input("Enter a string to check whether its palindrome or not : = ")

reverse_str=str_input[::-1]

print("String is palindrome" if str_input==reverse_str else "String is not palindrome")