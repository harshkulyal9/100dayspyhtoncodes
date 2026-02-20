def student(name,age):
    print(f"Name:,{name}")
    print("age:",age)

student(age=18,name="anuj")

def greet(name="student"):
    print("hello",name)
greet("aman")
greet()

def total(*num):
    sum=0
    for i in num:
        sum=sum+i
    print(f"{sum}")
total(10,20,30)
total(10,20)