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

def update_student():
    print("\n========== Update Student ==========")

    roll_no = input("Enter Roll Number to update: ")

    for student in students:
        if student.roll_no == roll_no:

            name = input("Enter New Name: ")
            if validate_name(name):
                student.name = name

            age = input("Enter New Age: ")
            if validate_age(age):
                student.age = int(age)

            gender = input("Enter New Gender (Male/Female/Other): ")
            if validate_gender(gender):
                student.gender = gender

            branch = input("Enter New Branch: ")
            if validate_branch(branch):
                student.branch = branch

            semester = input("Enter New Semester: ")
            if validate_semester(semester):
                student.semester = int(semester)

            cgpa = input("Enter New CGPA: ")
            if validate_cgpa(cgpa):
                student.cgpa = float(cgpa)

            phone = input("Enter New Phone Number: ")
            if validate_phone(phone):
                student.phone = phone

            email = input("Enter New Email: ")
            if validate_email(email):
                student.email = email

            address = input("Enter New Address: ")
            if validate_address(address):
                student.address = address

            save_students(students)

            print("\nStudent updated successfully.")
            return

    print("Student not found.")