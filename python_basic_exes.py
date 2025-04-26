
#ex1
gross_salary=int(input("enter your monthly gross salary: "))
net_income=gross_salary-(gross_salary*0.22)
rent=3000

if net_income >= rent and net_income-rent>=1000:
    print("Rent and save!")
elif net_income >= rent:
    print("Just rent.")
else:
    print("Not enough.")


#ex2
item_price = int(input("enter item price: "))
quantity = int(input("enter quantity: "))

total_price = item_price*quantity
is_shipping_fee_applied = False
is_discount_applied = False

if total_price <= 200:
    total_price+=20
    is_shipping_fee_applied=True
    print("shipping fee applied")
else:
    print("no shipping fee")

if total_price > 500:
    total_price*=0.90
    is_discount_applied = True
    print("discount applied")
else:
    print("no discount")

print(f"total price: {total_price}")


#ex3

age = 20
has_gold_pass = True 
is_royal = False
is_blacklisted = False 

if age >= 18 and (has_gold_pass or is_royal) and not is_blacklisted:    
    print("allowed")
else:
    print("not allowed")


#ex4

accident_count=3
age=23
base_premium=0

if age < 25:
    base_premium = 3000
else:
    base_premium = 2000

base_premium = base_premium + (500*accident_count)
if base_premium > 5000:
     print("High Risk")
else:
    print("Standard")

#ex5

temperature=33
pressure=24
voltage=210

if temperature >= 20 and temperature <= 80 and pressure < 50 and voltage >= 200 and voltage <= 250:
     print("Safe to proceed")
else:
     print("Unsafe conditions")


#ex6

spell_power = 93
accuracy = 72
control = 20
grade = ""

if spell_power < 40 or accuracy < 40 or control < 40:
    grade = "Fail"
else:
    average = (spell_power + accuracy + control)/3
    if average >= 90:
        grade = "Archmage"
    elif average > 74 and average < 90:
        grade = "Mage"
    elif average > 59 and average < 75:
        grade = "Apprentice"
    else:
        grade = "Fail"

print("grade: " + grade)
