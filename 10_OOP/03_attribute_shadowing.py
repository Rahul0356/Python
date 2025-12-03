class Chai:
    temp = "hot"
    strength = "Strong"

cutting = Chai()
print(cutting.temp) 

cutting.temp = "Mild"
print("After changing",cutting.temp)
print("Direct look into the class",Chai.temp)

del cutting.temp
print(cutting.temp)