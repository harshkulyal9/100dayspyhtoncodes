#Write a program to find the sum of digits of a number.
n=int(input("enter the number:"))

last_digit=0
sum=0
while(n!=0):
    last_digit=n%10
    sum+=last_digit
    n=n//10

print(f"the sum is:{sum}")