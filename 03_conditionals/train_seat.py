seat_type=input("Enter seat type (sleeper/Ac/general/luxury)").lower()

match seat_type:
  case "sleeper":
    print("Sleeper - No AC, beds available")

  case "ac":
    print("AC - Air conditioned, comfy ride")
  case "general":
    print("General - Cheapest option ,no reservation")
  case "luxuary":
    print("Luxury-Premium seats with meals")
  case _:
    print("Invalied seat type")