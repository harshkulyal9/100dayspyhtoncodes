#Write a program to swap two numbers using a third variable.

num_1=int(input("enter the first number:"))
num_2=int(input("enter the second number:"))

temp=0

temp=num_1
num_1=num_2
num_2=temp

print(f"first number after swaping is :{num_1}")
print(f"second number after swaping is :{num_2}")