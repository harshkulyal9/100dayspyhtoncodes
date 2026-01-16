#Write a program to calculate the area and perimeter of a rectangle given its length and breadth.

length=float(input("enter the length:"))
breadth=float(input("enter the breadth:"))

area=length*breadth
perimeter=2*(length+breadth)

print(f"the area of rectangle is:{area}")
print(f"the perimeter of recatangle is:{perimeter}")