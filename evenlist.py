#evenlist
n=int(input("enter the number:"))
l=[]
for i in range(1,n):
    if i%2==0:
        l.append(i)

print(f"the list of even number is:{l}")