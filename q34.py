#Write a program to check if a number is prime
n=int(input("enter the number:"))
a=1
for i in range (2,n):
    if(n%i==0):
        a=1
        break
    else:
        a=0
if a==0:
    print(f"prime number")
else:
    print(f"not prime number")
      