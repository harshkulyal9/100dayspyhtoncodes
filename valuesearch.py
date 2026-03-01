target=int(input("enter the finding value:"))
l=[1,2,3,4]
found=0
for i in l:
    if(l[i]==target):
        print(F"value found at index:{i}")
        found=0
        break
if (found==1):
    print(f"value not found")