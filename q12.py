#Write a program to input an integer and check whether it is positive, negative or zero using nested if–else.

n=int(input("enter the number:"))

if n<0:
    print(f"negative number")
elif n>0:
    print(f"positive number")
else:
    print(f"zero")    
