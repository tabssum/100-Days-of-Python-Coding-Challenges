try:
    num = int(input("Enter a number to find factorial: "))
    if num < 0:
        print("Factorial is not defined for negative numbers.")
    else:
        fact = 1
        for i in range(num, 0, -1):
            fact *= i
        print(f"Factorial of a number {num} is : {fact}")
except ValueError:
    print("Invalid input. Please enter a valid integer.")