#Write a program to classify a triangle as Equilateral, Isosceles, or Scalene based on its side lengths.

a=float(input("enter the first side of triangle :"))
b=float(input("enter the second side of triangle:"))
c=float(input("enter the third side of triangle:"))

if a==b and a==c and b==c:
    print(f"equilateral triangle")
elif a==b or b==c or a==c:
    print(f"issoclese triangle")
elif a!=b and a!=c and b!=c:
    print(f"scalene triangle ")
else:
    print(f"invalid")