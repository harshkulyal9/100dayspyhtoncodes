#square list
n=int(input("enter the size of list:"))
l=[]
for i  in range (n):
    value=int(input(""))
    l.append(value)

l1=[]
for i in l:
    val=i*i
    l1.append(val)

print(F'{l1}')