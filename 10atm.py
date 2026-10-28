# ATM

# A customer can withdraw money only when the ATM is not out of service. Write a python program to
# check if the customer can withdraw money.

atm_status = input("Is the ATM out of service? (yes/no): ").strip().lower()

if atm_status == 'no':
    print("The customer can withdraw money.")
else:
    print("The customer cannot withdraw money.")