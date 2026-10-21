try:
    number=int(input("Enter a number:= "))
    res="Number is even" if number%2==0 else "Number is odd"
    print(res)
except ValueError:
    print("Invalid input. Please enter a valid integer.")