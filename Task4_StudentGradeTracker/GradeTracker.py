def calculate_average(grades):
    return sum(grades) / len(grades) if grades else 0

def student_grade_tracker():
    subjects = []
    grades = []

    print("Welcome to the Student Grade Tracker!")

    while True:
        print("\nSelect your option:")
        print("1. Add Subject and Grade")
        print("2. Calculate Average Grade")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            subject = input("Enter the subject name: ")
            grade = float(input("Enter the grade for {}: ".format(subject)))
            subjects.append(subject)
            grades.append(grade)
            print("Grade added for", subject)

        elif choice == '2':
            if not grades:
                print("No grades added yet.")
            else:
                for i, subject in enumerate(subjects):
                    print("Grade for {}: {:.2f}".format(subject, grades[i]))
                print("Average Grade: {:.2f}".format(calculate_average(grades)))

        elif choice == '3':
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a valid option.")

student_grade_tracker()
