# Accept a string and delete all characters whose indices are divisible by 3.

# #Does not work if the string is too long 
# s = input("Enter a string: ")

# s = s[1:3] + s[4:6] + s[7:9] + s[10:]

# print(s)

#works for any length of string

s = input("Enter a string: ")
result = ""

for i in range(len(s)):
    if i % 3 != 0:
        result += s[i]

print(result)