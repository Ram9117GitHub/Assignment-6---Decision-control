''''Write a python script to print two given words in dictionary order'''
print("Enter two city names:")
first = input("Enter first word :")
second = input("Enter second word :")
if first>second:
    print(first,second)
else:
    print(second,first)