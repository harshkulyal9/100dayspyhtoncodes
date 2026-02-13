def fibo(a):
    if a<=1:
        return a
    else:
        return fibo(a-1)+fibo(a-2)
   
n=int(input("enter the number:"))
 
print(f"the fibo number is:{fibo(n)}")