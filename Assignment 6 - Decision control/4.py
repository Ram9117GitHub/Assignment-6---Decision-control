''''Write a python script to print greater between two numbers. Print number only once even if the numbers are the same.'''
num1 = int(input("Enter first number :"))
num2 = int(input("Enter second number :"))
if num1 > num2:
    if num1 % 2==0:
        print("number only even")
    else:
        print("First number is greater ",num1)
elif num1 == num2:
    print("The numbers are the same")
elif num1<num2:
    if num2 % 2 == 0:
        print("Number only even")
    else:
        print("Second number is greater",num2)

