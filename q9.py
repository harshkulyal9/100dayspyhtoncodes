#Write a program to calculate simple and compound interest for given principal, rate, and time.
principle=float(input("enter the principle:"))
rate=float(input("enter the rate:"))
time=float(input("enter the time:"))

simple_interest=float(principle*rate*time)/100
amount=principle*pow(1+rate/100,time)
compound_interest=amount-principle

print(f"the simple interest is :{ simple_interest}")
print(f"the compound interest is :{compound_interest}")