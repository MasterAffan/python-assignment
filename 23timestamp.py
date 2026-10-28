
# Write a Python program to read two timestamps in hours, minutes and seconds and calculate the
# absolute difference between them in seconds.

h1 = int(input("Hours 1: "))
m1 = int(input("Minutes 1: "))
s1 = int(input("Seconds 1: "))

h2 = int(input("Hours 2: "))
m2 = int(input("Minutes 2: "))
s2 = int(input("Seconds 2: "))

time1 = h1 * 3600 + m1 * 60 + s1
time2 = h2 * 3600 + m2 * 60 + s2

difference = abs(time1 - time2)

print("Difference in seconds =", difference)

