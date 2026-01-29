#Write a program to print the sum of the first n odd numbers.
n=int(input("enter the number:"))

for i in range(1,n+1):
    if(i%2!=0):
        print(f"{i}")