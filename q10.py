#Write a program to input time in seconds and convert it to hours:minutes:seconds format.

total_seconds=int(input("enter the seconds:"))

hours=total_seconds//3600
minutes=(total_seconds%3600)//60
total_second=(total_seconds%60)

print(f"time={hours}:{minutes}:{total_second}")