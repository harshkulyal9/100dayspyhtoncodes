n=int(input("enter the number:"))
flag=1
for i in range(2,n):
    if (n%i==0):
        flag=0
    break
if flag==1:
    print(f"prime number")
else:
    print(f"composite number")
