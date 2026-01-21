#Write a program to input a year and check whether it is a leap year or not using conditional statements.

n=int(input("enter the year:"))

if n%400==0 or ( n%400==0 and n%100!=0):
    print(f"leap year")
else:
    print(f"not leap year")    