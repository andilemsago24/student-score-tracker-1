from students import add_student, view_students, search_student
from scores import calculate_average, highest_score, lowest_score


while True:
    print("\nMenu")
    print("1. Add student")
    print("2. View students")
    print("3. Search student")
    print("4. Calculate average")
    print("5. Highest score")
    print("6. Lowest score")
    print("7. Exit")

    choice = input("Enter your choice (1-7): ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        calculate_average()

    elif choice == "5":
        highest_score()

    elif choice == "6":
        lowest_score()

    elif choice == "7":
        print("Thank you for using the Student Score Tracker.")
        break

    else:
        print("Invalid choice. Please try again.")