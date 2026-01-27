#Write a program to implement a basic calculator using switch-case for +, -, *, /, %.

operator=input("Enter the operator:")
a=float(input("enter the first number:"))
b=float(input("enter the second number:"))

match operator:
    case "+":
        print(f"the sum is :{a+b}")
    case "-":
        print(f"the diffrence is: {a-b}") 
    case "/":
        print(f"the quotient is : {a//b} ")   
    case "*":
        print(f"the product is: {a*b}")