users = [
    {"id":1, "total":100,"Coupon": "P20"},
    {"id":2, "total":150,"Coupon": "F20"},
    {"id":3, "total":200,"Coupon": "A50"},
]
discounts = {
    "P20":(0.2,0),
    "F20":(0.5,0),
    "A50":(0,10)
}
for user in users:
    percent, fixed = discounts.get (user["coupon"],(0,0))
    discount = user["total"] * percent + fixed
    print (f"{user["id"] } paid {user["total"]} and got
    discount for next visit of rupees{discount}")