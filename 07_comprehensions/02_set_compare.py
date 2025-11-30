favourite_chais = [
    "Masala Chai", "Green Tea", "Masala Chai",
    "Lemon Tea", "Green Tea", "Elaichi Chai"
]

unique_chai = { chai for chai in favourite_chais}
print(unique_chai) 

recipes = {
    "Masala Chai": ["ginger","caradom","clove"],
    "Elaichi chai": ["cardamom", "milk"],
    "Spicy chai": ["ginger", "back pepper","clove"],
}
unique_spices ={spice for ingredients in recipes.values()
                for spice in ingredients}

print(unique_spices)
