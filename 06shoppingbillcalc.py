price_of_one_item = int(input("Enter price of one: "))
quantity = int(input("Enter quantity purchased: "))
discount = int(input("Enter discount: "))
delivery_charge = int(input("Enter delivery charge: "))
number_of_friends = int(input("Enter number of friends sharing bill: "))
subtotal = (price_of_one_item * quantity) + delivery_charge
total = (subtotal/100) * (100 - discount)
per_person = total / number_of_friends

print(f"The total is {total}")
print(f"Each pays {per_person}")

