#Write a program to swap two numbers without using a third variable.

num_1=int(input("enter the first number:"))
num_2=int(input("enter the second number: "))

num_1=num_1+num_2
num_2=num_1-num_2
num_1=num_1-num_2


print(f"first number after swaping is {num_1}")
print(f"second number after swaping is {num_2}")