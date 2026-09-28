
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