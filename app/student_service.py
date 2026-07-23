from app.student import Student
from app.file_manager import load_students, save_students
from app.validator import *

students = load_students()

def add_student():
    print("\n========== Add Student ==========")

    roll_no = input("Enter Roll Number: ")

    if not validate_roll_no(roll_no):
        print("Invalid Roll Number.")
        return

    for student in students:
        if student.roll_no == roll_no:
            print("Roll Number already exists.")
            return

    name = input("Enter Name: ")
    if not validate_name(name):
        print("Invalid Name.")
        return

    age = input("Enter Age: ")
    if not validate_age(age):
        print("Invalid Age.")
        return

    gender = input("Enter Gender (Male/Female/Other): ")
    if not validate_gender(gender):
        print("Invalid Gender.")
        return

    branch = input("Enter Branch: ")
    if not validate_branch(branch):
        print("Invalid Branch.")
        return

    semester = input("Enter Semester: ")
    if not validate_semester(semester):
        print("Invalid Semester.")
        return

    cgpa = input("Enter CGPA: ")
    if not validate_cgpa(cgpa):
        print("Invalid CGPA.")
        return

    phone = input("Enter Phone Number: ")
    if not validate_phone(phone):
        print("Invalid Phone Number.")
        return

    email = input("Enter Email: ")
    if not validate_email(email):
        print("Invalid Email.")
        return

    address = input("Enter Address: ")
    if not validate_address(address):
        print("Invalid Address.")
        return

    student = Student(
        roll_no,
        name,
        int(age),
        gender,
        branch,
        int(semester),
        float(cgpa),
        phone,
        email,
        address
    )

    students.append(student)

    save_students(students)

    print("\nStudent added successfully.")

def view_students():
    print("\n========== Student List ==========")

    if not students:
        print("No students found.")
        return

    for student in students:
        student.display()

def search_student():
    print("\n========== Search Student ==========")

    roll_no = input("Enter Roll Number to search: ")

    for student in students:
        if student.roll_no == roll_no:
            print("\nStudent Found\n")
            student.display()
            return

    print("Student not found.")