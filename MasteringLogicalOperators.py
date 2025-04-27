
# ex1

# 1. 5 > 3 and 2 < 4 true
#  2. 10 == 2 * 5 or 3 != 3 true
#  3. not (7 <= 7 and 4 > 1) false
#  4. ("a" == "A").lower() and 0 false
#  5. 5 < 3 or (8 / 2 == 4 and not False) true


# ex2

# x>=10 and x<=20
# len(s) > 0 and s.count("py") > 0
# n < 0 or abs(n) > 100
# (user_role == "admin" and active == True) or superuser == True
# not (temperature < 0 or temperature > 35)


# ex3

age = int(input("enter your age: \n"))
has_ticket = input("do you has a ticket? (y/n)\n").lower()
vip_code = input("enter vip code: ")
eligible = False

if age < 0:
    print("Invalid age")
else:
    if (age >= 18 and has_ticket == "y") or vip_code == "GOLDVIP":
        eligible = True
    print(f"Access granted: {eligible}")


# ex4

username = input("enter username: ")
password = input("enter password: ")
email = input("enter email: ")

if len(username) > 0 and len(password) >= 8 and any(char.isdigit() for char in password)\
      and email.count("@") == 1 and email.endswith(".com"):
    print("Form valid")
else:
    print("Form invalid")

# ex5

order_amount = float(input("enter order amount: \n"))
customer_type = input("enter one customer type from these: regular, member or vip\n")
coupon_code = input("enter coupon_code: ")
total = 436

if order_amount < 50:
    total = total*1.05
if customer_type == "member" or customer_type == "vip":
    total = total*0.9
if customer_type == "vip" and coupon_code == "SAVE15":
    total = total*0.85

print(f"Final total: ${round(total,2)}")
