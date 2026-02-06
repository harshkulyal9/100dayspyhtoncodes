#Write a program to find the LCM of two numbers.
num1=int(input("enter the first number:"))
num2=int(input("enter the second nuber:"))
lcm=1
i=1
h=max(num1,num2)
while(i<num1*num2):
    if(i%num1==0 and i%num2==0):
     lcm=i
     break
    i=i+1

print(f"the lcm is :{lcm}")

