#basic calculator
operator=input("enter the type of arthmetic operator:")
a=int(input("enter the value of first number:"))
b=int(input("enter the value of second number:"))
match operator:
    case "+":
        print(f"addition {a+b}")
    case "-":
        print(f"substraction {a-b}")
    case "/":
        print(f"division {a/b}")
    case "*":
        print(f"multiplication {a*b}")
  
        