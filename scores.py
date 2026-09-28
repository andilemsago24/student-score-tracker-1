
def calculate_average():
    if len(students) == 0:
        print("No students available.")
    else:
        total = sum(students.values())
        average = total / len(students)
        print("Average Score:", average)


def highest_score():
    if len(students) == 0:
        print("No students available.")
    else:
        highest = max(students, key=students.get)

        print("Highest Score")
        print("Name:", highest)
        print("Score:", students[highest])


def lowest_score():
    if len(students) == 0:
        print("No students available.")
    else:
        lowest = min(students, key=students.get)

        print("Lowest Score")
        print("Name:", lowest)
        print("Score:", students[lowest]
              
              students = {}


def add_student():
    name = input("Enter student name: ")

    if name in students:
        print("Student already exists.")
    else:
        score = float(input("Enter student score: "))
        students[name] = score
        print("Student added successfully!")


def view_students():
    if len(students) == 0:
        print("No students found.")
    else:
        print("\n--- Student List ---")

        for name, score in students.items():
            print("Name:", name, "| Score:", score)


def search_student():
    name = input("Enter student name: ")

    if name in students:
        print("Student found")
        print("Name:", name)
        print("Score:", students[name])
    else:
        print("Student not found.")