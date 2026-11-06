import json
from pathlib import Path

# اسم ملف حفظ بيانات الطلاب
DATA_FILE = Path("students.json")


# تحميل بيانات الطلاب
def load_students():
    if DATA_FILE.exists():
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            return json.load(file)

    return []


# حفظ بيانات الطلاب
def save_students(students):
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(students, file, ensure_ascii=False, indent=4)


# إضافة طالب جديد
def add_student(students):
    name = input("Enter student name: ").strip()

    if not name:
        print("Name cannot be empty.")
        return

    try:
        grade = float(input("Enter student grade (0-100): "))

        if grade < 0 or grade > 100:
            print("Grade must be between 0 and 100.")
            return

    except ValueError:
        print("Please enter a valid number.")
        return

    status = "Passed" if grade >= 50 else "Failed"

    student = {
        "name": name,
        "grade": grade,
        "status": status
    }

    students.append(student)
    save_students(students)

    print("Student added successfully!")
    print("Result:", status)


# عرض جميع الطلاب
def show_students(students):
    if not students:
        print("No students found.")
        return

    print("\n--- Student List ---")

    for number, student in enumerate(students, start=1):
        print(
            number,
            "| Name:", student["name"],
            "| Grade:", student["grade"],
            "| Status:", student["status"]
        )


# البحث عن طالب
def search_student(students):
    name = input("Enter student name to search: ").strip().lower()

    found = False

    for student in students:
        if name in student["name"].lower():
            print("Name:", student["name"])
            print("Grade:", student["grade"])
            print("Status:", student["status"])
            found = True

    if not found:
        print("Student not found.")


# حساب متوسط الدرجات
def calculate_average(students):
    if not students:
        print("No grades available.")
        return

    total = sum(student["grade"] for student in students)
    average = total / len(students)
    print("Average grade:", round(average, 2))


# البرنامج الرئيسي
def main():
    students = load_students()

    while True:
        print("\n===== STUDENT MANAGEMENT SYSTEM =====")
        print("1. Add student")
        print("2. Show all students")
        print("3. Search for a student")
        print("4. Calculate average grade")
        print("5. Exit")

        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            add_student(students)

        elif choice == "2":
            show_students(students)

        elif choice == "3":
            search_student(students)

        elif choice == "4":
            calculate_average(students)

        elif choice == "5":
            print("Thank you for using the system!")
            break

        else:
            print("Invalid choice. Please choose from 1 to 5.")


if __name__ == "__main__":
    main()