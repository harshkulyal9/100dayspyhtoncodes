#Write a program to reverse a given number.
n=int(input("enter the number:"))
r=0
i=0
while n!=0:
    r=r+n%10
    r=r*10
    n=n//10
r=r//10

print(f"the reverse of number is:{r}")
