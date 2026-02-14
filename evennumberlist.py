#Create a list of even numbers from 1 to 20

list=[]

for j in range(1,20):
        if j%2==0:
            list.append(j)
print(f"the list of even number is:{list}")