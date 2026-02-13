def fact(a):
    if a==1:
        return 1
    else:
        return a*fact(a-1)

n=int(input("enter the number:"))
print(f"the factorial of number is:{fact(n)}")