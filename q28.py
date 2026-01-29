#Write a program to print the product of even numbers from 1 to n.
n=int(input("enter the number:"))

product=1
for i in range(1,n+1):
    if(i%2==0):
        product*=i

print(f"product of even number is : {product}")