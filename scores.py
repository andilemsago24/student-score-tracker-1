
students = {}


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
        print("Score:", students[lowest])


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
            print(f"Name: {name} | Score: {score}")


def search_student():
    name = input("Enter student name: ")
    if name in students:
        print("Student found")
        print("Name:", name)
        print("Score:", students[name])
    else:
        print("Student not found.")


def update_student():
    name = input("Enter student name to update: ")
    if name in students:
        score = float(input("Enter new score: "))
        students[name] = score
        print("Student updated successfully!")
    else:
        print("Student not found.")


def delete_student():
    name = input("Enter student name to delete: ")
    if name in students:
        del students[name]
        print("Student deleted successfully!")
    else:
        print("Student not found.")


def show_menu():
    print("\n=== Student Score Tracker ===")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Calculate Average")
    print("7. Highest Score")
    print("8. Lowest Score")
    print("9. Exit")


def main():
    while True:
        show_menu()
        choice = input("Enter choice (1-9): ")
        
        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            search_student()
        elif choice == '4':
            update_student()
        elif choice == '5':
            delete_student()
        elif choice == '6':
            calculate_average()
        elif choice == '7':
            highest_score()
        elif choice == '8':
            lowest_score()
        elif choice == '9':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()