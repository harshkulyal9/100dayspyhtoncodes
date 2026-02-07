#Write a program to find the product of odd digits of a number.
num=int(input("enter the number:"))
last_digit=0
product=1

while(num!=0):
    last_digit=num%10
    if(last_digit%2!=0):
        product=product*last_digit
    num=num//10


print(f"the product of odd digits are:{product}")