#Write a program to swap the first and last digit of a number.
n = input("Enter a number: ")

if len(n) > 1:
    swapped = n[-1] + n[1:-1] + n[0]
    print("Number after swapping:", swapped)
else:
    print("Number after swapping:", n)
