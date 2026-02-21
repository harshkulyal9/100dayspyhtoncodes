def num(a,pow):
    if pow==0:
        return 1
    else:
        return a*num(a,pow-1)
n=int(input("enter the number:"))
power=int(input("enter the exponent:"))
print(f"the value is:{num(n,power)}")