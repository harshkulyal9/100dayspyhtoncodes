#Write a program to find the roots of a quadratic equation and categorize them.
import math
import cmath


a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))


if a == 0:
    print("This is not a quadratic equation.")
else:

    d = b**2 - 4*a*c

    print(f"Discriminant = {d}")

    if d > 0:
       
        root1 = (-b + math.sqrt(d)) / (2*a)
        root2 = (-b - math.sqrt(d)) / (2*a)
        print("Roots are real and distinct.")
        print("Root 1:", root1)
        print("Root 2:", root2)

    elif d == 0:
       
        root = -b / (2*a)
        print("Roots are real and equal.")
        print("Root:", root)

    else:
       
        root1 = (-b + cmath.sqrt(d)) / (2*a)
        root2 = (-b - cmath.sqrt(d)) / (2*a)
        print("Roots are complex and imaginary.")
        print("Root 1:", root1)
        print("Root 2:", root2)
