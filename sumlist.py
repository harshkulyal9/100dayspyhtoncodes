def sum(n):
    list=(1,2,3,4)
    for i in range (0,len(list)):
        for j in range (1,len(list)):
            if list[i]+list[j]==n:
                return list[i],list[j]
            

print(f"{sum(3)}")            