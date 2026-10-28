email = input("Enter email address: ")

position = email.find("@")
username = email[:position]

print("Username =", username)