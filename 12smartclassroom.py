# Smart classroom:

# A Smart classroom uses a microcontroller to control a light, fan and projector. Write a python program
# to perform following conditions:

# a) Switch ON the Projector

# b) Check if Light is ON

# c) Toggle the status of Fan

# Assume Bit 0 = Light, Bit 1 = Fan, Bit 2 = Projector

status = 0b011   # Light = ON, Fan = ON, Projector = OFF

# a) Switch ON the Projector (Bit 2)
status = status | (1 << 2)

# b) Check if Light is ON (Bit 0)
if status & (1 << 0):
    print("Light is ON")
else:
    print("Light is OFF")

# c) Toggle the status of Fan (Bit 1)
status = status ^ (1 << 1)

# Display updated status
print("Updated Status:", bin(status))