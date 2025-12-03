chai_menu = {"masala":30, "ginger":25}

try:
  chai_menu["elaichi"]
except KeyError:
  print("The key that  you are typing to acress does not exists")

print("Hello Chai code")