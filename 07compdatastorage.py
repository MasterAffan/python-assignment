#Computer Data Storage Growth:

# Suppose computer system has initial storage eapacity of 8 GB. Its storage capacity doubles with every
# upgrade. Write a Python program to ealculate the total storage capacity after 4 upgrades.

initial_storage = 8 
number_of_upgrades = 4

total_storage = initial_storage * (2 ** number_of_upgrades)
print(f"The total storage capacity after {number_of_upgrades} upgrades is {total_storage} GB")

