# Student Eligibility:

# Write a python program to find out student is eligible for exam or not. Student is eligible for exam if
# student attendance is at least 75 % or student got special permission from director Sir.

attendance_percentage = float(input("Enter the student's attendance percentage: "))
special_permision = input("Does the student have special permission from director Sir? (yes/no): ").strip().lower()

if attendance_percentage >= 75 or special_permision == 'yes':
    print("The student is eligible for the exam.")
else:
    print("The student is not eligible for the exam.")
    