staff = [("Rahul",16),("Arya",20),("Raj",10)]

for name , age in staff:
    if age <= 18:
        print (f"{name} is eligible to manage the staff")
        break
    else :
        print(f"No one is eligible to mange the staff")
        