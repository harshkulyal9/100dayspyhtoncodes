n=int(input("enter the number:"))
num=n

r=0
while n!=0:
    r=r+n%10
    r=r*10
    n=n//10
r=r//10

if num==r:
    print(f"palindrome number")
else:
    print(f"not palindrome")
