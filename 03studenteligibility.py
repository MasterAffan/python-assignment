marks = int(input("Enter marks: "))
if marks >=40:
    status = "Passed"
else:
    status = "Failed"
if marks >= 60:
    status_60 = "Greater than 60 or equal to 60"
print(f"The student {status}")
print(f"{status_60}")