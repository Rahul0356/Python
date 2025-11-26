ingredients = ["water","milk","black tea"]

ingredients.append("suger")

print(f"Ingredients are:{ingredients}")

ingredients.remove("milk")

spice_options = ["ginger","cardamom"]
chai_ingredients =["water","milk"]

chai_ingredients.extend(spice_options)
print(f"chai:{chai_ingredients}")
chai_ingredients.insert(2,"black tea")
print(f"chai after inserting black tea:{chai_ingredients}")