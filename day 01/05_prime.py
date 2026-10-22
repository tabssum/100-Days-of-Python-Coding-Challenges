#Check whether number is prime or not
try:
    number = int(input("Enter a number to check whether its prime or not : = "))
    if number < 2:
        print("Number is not prime")
    else:
        for i in range(2,int(number**0.5)+1):
            if number % i ==0:
                print("Number is not prime")
                break
        else:
            print("Number is prime")
except ValueError:
    print("Please enter integer number")