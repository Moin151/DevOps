# # Task 1: Grade Checker
# score = float(input("Enter the student's score: "))
# if score >= 90:
#     print("Grade: A")
# elif score >= 80:
#     print("Grade: B")
# elif score >= 70:
#     print("Grade: C")
# elif score >= 60:
#     print("Grade: D")
# else:
#     print("Grade: F")


# Task 2: Student Grades Management
# student_grades = {}

# # 1. Add a new student and grade
# student_grades["Student1"] = "A"
# student_grades["Student2"] = "B"
# print("After adding students:", student_grades)

# # 2. Update an existing student's grade
# student_name = "Student2"
# if student_name in student_grades:
#     student_grades[student_name] = "A"  # Upgraded Bob to A
#     print(f"Updated {student_name}'s grade.")

# # 3. Print all student grades
# print("\n--- All Student Grades ---")
# for name, grade in student_grades.items():
#     print(f"{name}: {grade}")

# Task 3: Write to a File
# file_name = "student_info.txt"

# with open(file_name, "w") as file:
#     file.write("Name: Student1, Grade: A\n")
#     file.write("Name: Student2, Grade: A\n")

# print(f"Successfully wrote data to {file_name}")


# Task 4: Read from a File
file_name = "student_info.txt"

with open(file_name, "r") as file:
    content = file.read()
    print("--- Reading File Content ---")
    print(content)