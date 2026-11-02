import re


class StudentManagementSystem:

    FILE_NAME = "students.txt"

    def create_login(self):
        print("\n========== CREATE ACCOUNT ==========")

        while True:
            username = input("Create Username: ")
            password = input("Create Password: ")

            # Username: letters, numbers and special characters allowed
            # Password: capital, small, numbers and special characters allowed

            if len(username) < 4:
                print("Username must contain at least 4 characters.")
                continue

            if len(password) < 8:
                print("Password must contain at least 8 characters.")
                continue

            if not re.search(r"[A-Z]", password):
                print("Password must contain at least one Capital letter.")
                continue

            if not re.search(r"[a-z]", password):
                print("Password must contain at least one Small letter.")
                continue

            if not re.search(r"[0-9]", password):
                print("Password must contain at least one Number.")
                continue

            if not re.search(r"[^A-Za-z0-9]", password):
                print("Password must contain at least one Special character.")
                continue

            print("\nAccount created successfully!")
            return username, password

    def login(self, username, password):
        print("\n========== LOGIN ==========")

        login_username = input("Enter Username: ")
        login_password = input("Enter Password: ")

        if login_username == username and login_password == password:
            print("\nLogin successful!")
            return True
        else:
            print("\nInvalid Username or Password!")
            return False

    def add_student(self):
        print("\n========== ADD STUDENT ==========")

        student_id = input("Enter Student ID: ")
        name = input("Enter Student Name: ")
        age = input("Enter Age: ")
        course = input("Enter Course: ")
        marks = input("Enter Marks: ")

        with open(self.FILE_NAME, "a") as file:
            file.write(
                f"{student_id},{name},{age},{course},{marks}\n"
            )

        print("Student added successfully!")

    def view_students(self):
        print("\n========== STUDENT DETAILS ==========")

        try:
            with open(self.FILE_NAME, "r") as file:
                students = file.readlines()

            if not students:
                print("No student records found.")
                return

            for student in students:
                data = student.strip().split(",")

                print("----------------------------")
                print("Student ID :", data[0])
                print("Name       :", data[1])
                print("Age        :", data[2])
                print("Course     :", data[3])
                print("Marks      :", data[4])

        except FileNotFoundError:
            print("No student records found.")

    def search_student(self):
        print("\n========== SEARCH STUDENT ==========")

        search_id = input("Enter Student ID: ")

        try:
            with open(self.FILE_NAME, "r") as file:
                for student in file:
                    data = student.strip().split(",")

                    if data[0] == search_id:
                        print("\nStudent Found!")
                        print("Student ID :", data[0])
                        print("Name       :", data[1])
                        print("Age        :", data[2])
                        print("Course     :", data[3])
                        print("Marks      :", data[4])
                        return

            print("Student not found.")

        except FileNotFoundError:
            print("No student records found.")

    def update_student(self):
        print("\n========== UPDATE STUDENT ==========")

        update_id = input("Enter Student ID: ")

        try:
            with open(self.FILE_NAME, "r") as file:
                students = file.readlines()

            found = False

            with open(self.FILE_NAME, "w") as file:
                for student in students:
                    data = student.strip().split(",")

                    if data[0] == update_id:
                        name = input("Enter New Name: ")
                        age = input("Enter New Age: ")
                        course = input("Enter New Course: ")
                        marks = input("Enter New Marks: ")

                        file.write(
                            f"{update_id},{name},{age},{course},{marks}\n"
                        )

                        found = True
                    else:
                        file.write(student)

            if found:
                print("Student updated successfully!")
            else:
                print("Student not found.")

        except FileNotFoundError:
            print("No student records found.")

    def delete_student(self):
        print("\n========== DELETE STUDENT ==========")

        delete_id = input("Enter Student ID: ")

        try:
            with open(self.FILE_NAME, "r") as file:
                students = file.readlines()

            found = False

            with open(self.FILE_NAME, "w") as file:
                for student in students:
                    data = student.strip().split(",")

                    if data[0] == delete_id:
                        found = True
                    else:
                        file.write(student)

            if found:
                print("Student deleted successfully!")
            else:
                print("Student not found.")

        except FileNotFoundError:
            print("No student records found.")

    def menu(self):
        while True:

            print("\n========== STUDENT MANAGEMENT SYSTEM ==========")
            print("1. Add Student")
            print("2. View Students")
            print("3. Search Student")
            print("4. Update Student")
            print("5. Delete Student")
            print("6. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.add_student()

            elif choice == "2":
                self.view_students()

            elif choice == "3":
                self.search_student()

            elif choice == "4":
                self.update_student()

            elif choice == "5":
                self.delete_student()

            elif choice == "6":
                print("\nThank you!")
                break

            else:
                print("Invalid choice!")


# Main Program

system = StudentManagementSystem()

username, password = system.create_login()

if system.login(username, password):
    system.menu()