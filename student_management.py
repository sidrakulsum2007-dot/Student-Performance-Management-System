# ================================================
# STUDENT PERFORMANCE MANAGEMENT SYSTEM
# ================================================

students = []


# ------------------------------------------------
# Function to calculate grade
# ------------------------------------------------
def calculate_grade(average):
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"


# ------------------------------------------------
# Function to add a student
# ------------------------------------------------
def add_student():
    print("\n---------- ADD STUDENT ----------")

    student_id = input("Enter Student ID: ")
    name = input("Enter Student Name: ")

    mark1 = float(input("Enter Subject 1 Marks: "))
    mark2 = float(input("Enter Subject 2 Marks: "))
    mark3 = float(input("Enter Subject 3 Marks: "))

    total = mark1 + mark2 + mark3
    average = total / 3
    grade = calculate_grade(average)

    student = {
        "id": student_id,
        "name": name,
        "marks": [mark1, mark2, mark3],
        "total": total,
        "average": average,
        "grade": grade
    }

    students.append(student)

    print("\nStudent added successfully!")
    print("Total Marks:", total)
    print("Average Marks:", round(average, 2))
    print("Grade:", grade)


# ------------------------------------------------
# Function to display all students
# ------------------------------------------------
def display_students():
    print("\n---------- STUDENT PERFORMANCE ----------")

    if len(students) == 0:
        print("No student records found.")
        return

    for student in students:
        print("\nStudent ID:", student["id"])
        print("Name:", student["name"])
        print("Marks:", student["marks"])
        print("Total Marks:", student["total"])
        print("Average Marks:", round(student["average"], 2))
        print("Grade:", student["grade"])
        print("----------------------------------------")


# ------------------------------------------------
# Function to update a student
# ------------------------------------------------
def update_student():
    print("\n---------- UPDATE STUDENT ----------")

    student_id = input("Enter Student ID to update: ")

    for student in students:
        if student["id"] == student_id:

            print("Current Name:", student["name"])

            name = input("Enter New Name: ")

            mark1 = float(input("Enter New Subject 1 Marks: "))
            mark2 = float(input("Enter New Subject 2 Marks: "))
            mark3 = float(input("Enter New Subject 3 Marks: "))

            total = mark1 + mark2 + mark3
            average = total / 3
            grade = calculate_grade(average)

            student["name"] = name
            student["marks"] = [mark1, mark2, mark3]
            student["total"] = total
            student["average"] = average
            student["grade"] = grade

            print("\nStudent record updated successfully!")
            return

    print("Student ID not found.")


# ------------------------------------------------
# Function to delete a student
# ------------------------------------------------
def delete_student():
    print("\n---------- DELETE STUDENT ----------")

    student_id = input("Enter Student ID to delete: ")

    for student in students:
        if student["id"] == student_id:
            students.remove(student)
            print("Student record deleted successfully!")
            return

    print("Student ID not found.")


# ------------------------------------------------
# Function to save students to a file
# ------------------------------------------------
def save_to_file():
    with open("students.txt", "w") as file:

        for student in students:
            file.write(
                student["id"] + "|" +
                student["name"] + "|" +
                str(student["marks"][0]) + "," +
                str(student["marks"][1]) + "," +
                str(student["marks"][2]) + "|" +
                str(student["total"]) + "|" +
                str(student["average"]) + "|" +
                student["grade"] + "\n"
            )

    print("Student records saved successfully!")


# ------------------------------------------------
# Function to load students from file
# ------------------------------------------------
def load_from_file():
    try:
        with open("students.txt", "r") as file:

            for line in file:
                data = line.strip().split("|")

                if len(data) == 6:
                    student_id = data[0]
                    name = data[1]

                    marks = [
                        float(data[2].split(",")[0]),
                        float(data[2].split(",")[1]),
                        float(data[2].split(",")[2])
                    ]

                    total = float(data[3])
                    average = float(data[4])
                    grade = data[5]

                    student = {
                        "id": student_id,
                        "name": name,
                        "marks": marks,
                        "total": total,
                        "average": average,
                        "grade": grade
                    }

                    students.append(student)

        print("Student records loaded from file.")

    except FileNotFoundError:
        print("No previous student records found.")


# ------------------------------------------------
# MAIN PROGRAM
# ------------------------------------------------

print("==============================================")
print("     STUDENT PERFORMANCE MANAGEMENT SYSTEM")
print("==============================================")


# Load previous records when program starts
load_from_file()


while True:

    print("\n============== MENU ==============")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Save Records to File")
    print("6. Exit")
    print("==================================")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        display_students()

    elif choice == "3":
        update_student()

    elif choice == "4":
        delete_student()

    elif choice == "5":
        save_to_file()

    elif choice == "6":
        save_to_file()
        print("\nThank you for using the Student Performance Management System!")
        break

    else:
        print("Invalid choice. Please enter a number from 1 to 6.")