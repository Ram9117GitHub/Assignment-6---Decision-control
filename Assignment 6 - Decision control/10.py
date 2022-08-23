'''Write a python script to print greater among three numbers. Print number only once even if the numbers are the same'''
num1 = int(input("Enter first number :"))
num2 = int(input("Enter second number :"))
num3 = int(input("Enter third number :"))
if num1 > num2:
    if num1 % 2 == 0:
        print("Even number is ",num1)
    print("num1")
elif num1 < num2:
    if num2 % 2 ==0:
        print("Even number is",num2)
    print(num2)
elif  num1 == num2 == num3:
    print("If the numbers are the same")
else:
    if num3 % 2 == 0:
        print("Even number is",num3)
    print(num3)
