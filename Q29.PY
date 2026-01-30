#Write a program to calculate the factorial of a number.
n=int(input("enter the number:"))
factorial=1
i=1
while i<=n:
    factorial*=i
    i=i+1
print(f"factorial of number is :{factorial}")