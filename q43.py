#Write a program to check if a number is a strong number.
num=int(input("enter the number:"))
sum=0
temp=num

while(temp!=0):
    last_digit=temp%10
    factorial=1
    for i in range(1,last_digit+1):
        factorial=factorial*i
    sum=sum+factorial
    temp=temp//10

if sum==num:
    print(f"strong number")
else:
    print(f"not strong number")

    