# Student Performance Management System

## Project Overview

The Student Performance Management System is a Python-based application developed to manage student academic records. It allows users to add, display, update, and delete student records, calculate student performance, assign grades, and store student information in a file.

## Objectives

* Manage student academic records efficiently.
* Calculate total and average marks.
* Assign grades automatically based on average marks.
* Display student performance details.
* Update and delete existing student records.
* Store and retrieve student records using file handling.

## Features

* Add Student
* Display Students
* Update Student
* Delete Student
* Calculate Total Marks
* Calculate Average Marks
* Assign Grades
* Save Records to File
* Retrieve Records from File

## Technologies Used

* Python
* Lists
* Dictionaries
* Functions
* Conditional Statements
* Loops
* File Handling
* Exception Handling

## Grading System

| Average Marks | Grade |
| ------------- | ----- |
| 90 and above  | A+    |
| 80–89         | A     |
| 70–79         | B     |
| 60–69         | C     |
| 50–59         | D     |
| Below 50      | F     |

## Project Structure

```text
Student-Performance-Management-System/
│
├── student_management.py
├── students.txt
└── screenshots/
    ├── Screenshot_01_Menu.png
    ├── Screenshot_02_Add_Display.png
    ├── Screenshot_03_Update.png
    ├── Screenshot_04_Delete.png
    ├── Screenshot_05_File_Save.png
    └── Screenshot_06_File_Retrieval.png
```

## How to Run

1. Open the project folder in VS Code.
2. Open the terminal.
3. Run the following command:

```bash
python student_management.py
```

4. Select the required option from the menu.
5. Add, display, update, or delete student records.
6. Use the save option to store student records in the file.
7. Restart the program to retrieve the saved records.

## Sample Operations

The system supports the following menu options:

1. Add Student
2. Display Students
3. Update Student
4. Delete Student
5. Save Records to File
6. Exit

## File Storage

Student records are stored in `students.txt`. The program can load previously saved records when it starts and save updated records when required.

## Project Outcome

The project successfully demonstrates student record management, performance calculation, automatic grading, and file-based storage and retrieval using Python.

## Conclusion

The Student Performance Management System provides a simple way to manage student academic information using Python programming concepts such as functions, lists, dictionaries, conditional statements, loops, and file handling.
