import json
import os

DATA_FILE = "students.json"

SUBJECTS = ("Python", "Mathematics", "Physics",
            "English", "Computer")

students = []


def load_data():
    global students
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            students = json.load(file)


def save_data():
    with open(DATA_FILE, "w") as file:
        json.dump(students, file, indent=4)


def calculate_result(marks):
    total = sum(marks.values())
    percentage = total / len(SUBJECTS)

    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 40:
        grade = "D"
    else:
        grade = "F"

    return total, percentage, grade


def add_student():
    roll = input("Enter Roll Number: ")
    name = input("Enter Student Name: ")

    marks = {}

    for subject in SUBJECTS:
        marks[subject] = float(
            input(f"Enter {subject} marks: ")
        )

    student = {
        "roll_no": roll, 
        "name": name,

        "marks": marks
    }

    students.append(student)
    save_data()

    print("Student added successfully!")


def display_students():
    for student in students:
        total, percentage, grade = calculate_result(
            student["marks"]
        )

        print("\nRoll No:", student["roll_no"])
        print("Name:", student["name"])
        print("Marks:", student["marks"])
        print("Total:", total)
        print("Percentage:", percentage)
        print("Grade:", grade)


def main():
    load_data()

    while True:
        print("\n1. Add Student")
        print("2. Display Students")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            display_students()

        elif choice == "3":
            save_data()
            print("Thank you!")
            break

        else:
            print("Invalid choice!")


main()