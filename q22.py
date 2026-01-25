#Write a program to find profit or loss given cost price and selling price.

cost_price=float(input("enter the cost price:"))
sell_price=float(input("enter the sell price:"))

if(sell_price>cost_price):
    print(f"profit: {sell_price -cost_price}")

if(cost_price>sell_price):
    print(f"loss: {cost_price - sell_price}")