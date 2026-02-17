def num(a):
    if a==0:
        return 
    else:
        print(f"{a}")
        num(a-1)
        return
    
n=int(input("enter the number:"))
num(n)