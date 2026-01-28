'''14. Write a program to find left shift and right shift values of a given number. 14.
Using membership operator find whether a given number is in sequence
(10,20,56,78,89)'''

sequence=(10,20,56,78,89)

num=int(input("enter the number want to find:"))

if num in sequence:
    print(f"number is in sequence")
else:
    print(f"not in sequence")