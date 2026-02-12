#1. Scan n values in range 0-3 and print the number of times each value has occurred
n=int(input("enter the number:"))
list=[]
for i in range(n):
    value=int(input())
    if value>=0 and value<=3:
     list.append(value)
    else:
        print(f"invalid")
  

count=0
count1=0
count2=0
for i in list:
    if i==1:
        count=count+1
    elif(i==2):
        count1=count1+1
    elif(i==3):
        count2=count2+1
    else:
        print(f"invalid")

if count==0:
    print(f"1 occured zero times")
else:
    print(f"1 occured is :{count}")

if count1==0:
    print(f"2 occured zero times")
else:
    print(f"2 occured is :{count1}")

if count==0:
    print(f" 3occured zero times")
else:
    print(f"3 occured is :{count2}")
