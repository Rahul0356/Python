order_amount = input ("Enter the oder amount:")

delivery_fees = 0 if order_amount > 300 else 30
print(f"Delivery fess is : {delivery_fees}")