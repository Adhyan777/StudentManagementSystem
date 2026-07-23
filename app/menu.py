from app.student_service import (
    add_student,
    view_students,
    search_student,
    update_student,
    delete_student,
    count_students
)


def show_menu():
    while True:
        print("\n" + "=" * 50)
        print("      STUDENT MANAGEMENT SYSTEM")
        print("=" * 50)
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Count Students")
        print("7. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            view_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            update_student()

        elif choice == "5":
            delete_student()

        elif choice == "6":
            count_students()

        elif choice == "7":
            print("\nThank you for using Student Management System.")
            break

        else:
            print("\nInvalid choice. Please try again.")