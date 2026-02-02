#Write a program to print all factors of a given number.
n=int(input("enter the number:"))
i=1
while i<=n:
    if(n%i==0):
        print(f"factors are: {i}")
    i=i+1
