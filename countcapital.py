#Write a program to count and display the number of capital letters in a given string
n=input("enter the string:")
count=0
for ch in n:
    if ch>='A' and ch<='Z':
        count=count+1

if count==0:
    print(f"no capital letter")
else:
    print(f"the number of capital letter are:{count}")
