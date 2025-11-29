flavours  = ["Ginger","Out of Stock","Lemon",
"Discontinued", "Tulsi"]

for flavour in flavours:
    if flavour == "Out of Stock":
        continue
    if flavour == "Discontinued":
        break
    print("Discountined item found")

    print(f"Out side of loop")
    

