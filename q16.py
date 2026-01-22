#Write a program to input three numbers and find the largest among them using if–else.
a=int(input("enter the first number:"))
b=int(input("enter the second number:"))
c=int(input("enter the third number:"))

if a>b and a>c:
    print(f"first number is largest")
elif b>a and b>c:
    print(f"second number is largest")
else:
    print(f"third number is largest")