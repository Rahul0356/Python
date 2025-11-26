essential_spices = {"cardamon","ginger","cinnamon"}
optional_spices = {"clover","ginger","black paper"}

all_spices = essential_spices | optional_spices
print(f"All spices needed for masala: {all_spices}")

common_spices = essential_spices & optional_spices
print(f"common spices:{common_spices}")

