# Students details list manager with file handling

import json
import os

FILE_NAME = "students.json"

# Load data from file
if os.path.exists(FILE_NAME):
    with open(FILE_NAME, "r") as file:
        try:
            students = json.load(file)
            students = {int(k): v for k, v in students.items()}
        except json.JSONDecodeError:
            students = {}
else:
    students = {}

# Save data to file
def save_to_file():
    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)

def input_enrollment():
    while True:
        try:
            enroll = int(input("Enter enrollment no. = "))
            if enroll > 0:
                return enroll
            print("Enrollment number must be positive!")
        except ValueError:
            print("Enter a valid integer!")

def input_phone():
    while True:
        phone = input("Enter phone no. (10 digits) = ")
        if phone.isdigit() and len(phone) == 10:
            return phone
        print("Invalid phone number! Must be 10 digits.")

def input_gmail():
    while True:
        gmail = input("Enter gmail (must end with @gmail.com) = ")
        if gmail.endswith("@gmail.com"):
            return gmail
        print("Invalid gmail! Must end with @gmail.com.")

def input_age():
    while True:
        try:
            age = int(input("Enter age = "))
            if age > 0:
                return age
            print("Age must be positive!")
        except ValueError:
            print("Enter a valid integer for age!")

while True:
    print("\nOperations can be performed are")
    print("1.Add new student details")
    print("2.Update old student details")
    print("3.Delete any student all details")
    print("4.Search any student details")
    print("5.Display all students details")
    print("6.Exit\n")

    try:
        choice = int(input("Enter your choice = "))
    except ValueError:
        print("Choice must be an integer!")
        continue

    match choice:
        case 1:
            enrollment_no = input_enrollment()
            if enrollment_no not in students:
                name = input("Enter name = ")
                phone_no=input_phone()
                age = input_age()
                gmail = input_gmail()

                students[enrollment_no] = {
                    "Name": name,
                    "Phone no": phone_no,
                    "Age": age,
                    "Gmail": gmail
                }
                save_to_file()
                print("Details added successfully!!")
            else:
                print("Enrollment no. already exists!!")

        case 2:
            enrollment_no = input_enrollment()
            if enrollment_no in students:
                while True:
                    print("\nFor Update")
                    print("1.Name")
                    print("2.Phone no.")
                    print("3.Age")
                    print("4.Gmail")
                    print("5.Done")

                    try:
                        point = int(input("Enter your choice = "))
                    except ValueError:
                        print("Enter valid integer choice!")
                        continue

                    match point:
                        case 1:
                            students[enrollment_no]["Name"] = input("Enter new name = ")
                        case 2:
                            students[enrollment_no]["Phone no"] = input("Enter new phone no = ")
                        case 3:
                            students[enrollment_no]["Age"] = int(input("Enter new age = "))
                        case 4:
                            students[enrollment_no]["Gmail"] = input("Enter new gmail = ")
                        case 5:
                            break
                        case _:
                            print("Invalid choice!")

                save_to_file()
                print("Details updated successfully!!")
            else:
                print("Enrollment no. not found!!")

        case 3:
            if not students:
                print("Students list is empty!!")
                continue

            enrollment_no = input_enrollment()
            if enrollment_no in students:
                students.pop(enrollment_no)
                save_to_file()
                print("Details deleted successfully!!")
            else:
                print("Enrollment no. not found!!")

        case 4:
            if not students:
                print("Students list is empty!!")
                continue

            enrollment_no = input_enrollment()
            if enrollment_no in students:
                print(students[enrollment_no])
            else:
                print("Enrollment no. not found!!")

        case 5:
            if not students:
                print("Students list is empty!!")
            else:
                for i, details in students.items():
                    print(f"\nEnrollment no = {i}")
                    for key, value in details.items():
                        print(f"{key} = {value}")

        case 6:
            print("Exiting program. Goodbye!")
            break

        case _:
            print("Invalid choice!")
