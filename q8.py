#Write a program to find and display the sum of the first n natural numbers.

n=int(input("enter the number :"))
sum=0
i=1
while(i<=n):
    sum+=i
    i+=1

print(f"the sum of n natural number is : {sum}")