# Write a Python program to find the roots of ax2 + bx + c = 0.

import cmath

a = float(input("Enter the coefficient a: "))
b = float(input("Enter the coefficient b: "))
c = float(input("Enter the coefficient c: "))

# Calculate the discriminant
d = (b**2) - (4*a*c)

# Find the two roots
root1 = (-b - cmath.sqrt(d)) / (2*a)
root2 = (-b + cmath.sqrt(d)) / (2*a)

print(f"The roots are {root1} and {root2}")