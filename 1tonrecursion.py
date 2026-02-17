#Write a Python function to print 1 to n using recursion
def num(a):
    if a==0:
        return
    else:
        num(a-1)
        print(f"{a}")
        return
    
n=int(input("enter the number:"))
num(n)
      

