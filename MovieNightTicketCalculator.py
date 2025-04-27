
age = int(input("Age? "))
if age < 0:
    print("Invalid age")

else:
    day = input("Day (weekday/weekend)? ").lower()
    if day != "weekday" and day != "weekend":
        print("Invalid day")
    else:
        loyalty_member = input("Loyalty member (y/n)? ").lower()
        base_price = 20
        price=0
        if age < 13:
            price = base_price*0.5
        elif age >= 60:
            price = base_price*0.7
        else:
            price = base_price

        if day == "weekend":
            price+=5
        if loyalty_member == "y":
            price-=2
        print(f"Total: ${price}")