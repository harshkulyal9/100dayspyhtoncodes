def cube(a):
    sum=0
    for i in range(1,a):
        sum+=i**3
    return sum

n=int(input("enter the number:"))
print(f"the sum of cube:{cube(n)}")
    
