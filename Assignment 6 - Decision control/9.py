'''Write a python script to check whether a given year is a leap year or not.'''
year = int(input("Enter a year :"))
if year % 4 ==0:
    print("Leap year",year)
else:
    print("Not Leap year",year)
""""""""and""""""""""""
year = int(input("Enter a year :"))
if year %400==0:
    print("Leap year",year)
else:
    print("Not Leap year ",year)
""""""""""""""""""and""""""""""""""""""
year = int(input("Enter a year :"))
if year %100!=0:
    print("Leap year",year)
else:
    print("Not Leap year",year)