order_amount=float(input("enter the order amount:"))
if order_amount>300:
   print(f"delivery is free")
else:
    print(f"delivery charge =30")

delivery_fees= 0 if order_amount> 300 else 30

print(f"delivery fees:{delivery_fees}")