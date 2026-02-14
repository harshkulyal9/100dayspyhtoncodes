#Find all pairs in a list whose sum equals a target value.
list=[1,2,3,4,5,5,6]
target=int(input("enter the target value:"))

for i in range(len(list)):
    for j in range(i+1,len(list)):
        if list[i]+list[j]==target:
         print(f"the pairs are:{list[i],list[j]}")