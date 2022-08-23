'''Write a python script to check whether a given number is a three digit number or not.'''
num = int(input("Enter a number :"))
if num<1000 and num > 99:
    print("Three digit number")
else:
    print("Not")