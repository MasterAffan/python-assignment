# Write a Python program to accept three numbers from the user and find the maximum number.

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

if num1 >= num2 and num1 >= num3:
    max_num = num1
elif num2 >= num1 and num2 >= num3:
    max_num = num2
else:
    max_num = num3

#Alternatively, you can use the built-in max() function to find the maximum number:
# max_num = max(num1, num2, num3)

print(f"The maximum number is: {max_num}")