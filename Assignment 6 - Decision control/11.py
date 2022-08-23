''''Write a python script to take the month value in numeric format and display the number of days in it.'''
month = int(input("Enter the number of month :"))
year = int(input("Enter a year :"))
if (month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12):
    print("Number of days is 31 ")
elif (month==2) and (year % 400==0) or (year % 4==0) or (year % 100 !=0):
    print("number of day is 29")
elif(month==2):
    print("Number of day is 28")
else:
    print("Number of days is 30")