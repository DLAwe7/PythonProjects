


student_data = []
students_list = [
    {"name": "Alice", "subjects": {"Math": 9.0, "Science": 8.5}},
    {"name": "Bob", "subjects": {"English": 7.5, "History": 6.0}}
]


def options():
    print("1. Add a new student\n"
          "2. View all students and grades\n"
          "3. Calculate a student's average grade\n"
          "4. View class average for a subject\n"
          "5. Modify student's profile\n"
      "6. Exit\n")

def student_add():
    student_name = input("Enter the student's name: ")
    subject_and_grade = input("Enter subjects and grades (e.g., Math:9, Science:8.5): ").capitalize().strip()

    subjects_and_grades = {}

    for item in subject_and_grade.split(", "):
        subject_name, grade = item.split(":")
        subjects_and_grades[subject_name] = float(grade)

    student_data = {"name": student_name, "subjects": subjects_and_grades}
    students_list.append(student_data)

    print("Student and grades added successfully")

def students_grades_display():
    for student in students_list:
        print(f"{student["name"]}")
        for subject, grade in student["subjects"].items():
            print(f"{subject}: {grade}")

def class_subject_average(subject_name, students_list):
    total = 0
    count = 0
    for student in students_list:
        if subject_name in student["subjects"]:
            total += student["subjects"][subject_name]
            count += 1
    if count > 0:
        return total / count
    else:
        return None



def class_average():
    for student in students_list:
            total = 0
            num_of_subjects = 0
            for subject, grade in student["subjects"].items():
                total += grade
                num_of_subjects += 1
            print(f"Your class average is: {total / num_of_subjects}")

def student_mod():
    student_name = input("Please enter student's name: ")
    for student in students_list:
        if student["name"] == student_name:
            choice = input("Would you like to remove or modify an existing student (Remove (R), Modify (M): ").lower()
            if choice == "m":
                subject_and_grade = input("Enter subjects and grades (e.g., Math:9, Science:8.5): ").capitalize()
                subjects_and_grades = {}
                for item in subject_and_grade.split(", "):
                    subject_name, grade = item.split(":")
                    subjects_and_grades[subject_name] = float(grade)

                student_data = {"name": student_name, "subjects": subjects_and_grades}
                students_list.append(student_data)
            print("Student successfully updated")

            if choice == "r":
                student_name = input("Please enter student's name: ")
                students_list.remove(student_name, "subjects")
                print(f"{student_name} has been removed from the list.")
            else:
                print(f"{user_input} is not a valid input. Please enter M or R to modify an existing student or remove it.")
            break
        else:
            print(f"{student_name} was not found")

def main():
    running = True
    while running:
        options()
        user_input = input("> ")
        match user_input:
            case "1":
                student_add()

            case "2":
                students_grades_display()

            case "3":
                class_subject_average()

            case "4":
                class_average()

            case "5":
                student_mod()

            case "6":
                print("Goodbye!")
                running = False
            case _:
                print(f"{user_input} isn't a valid input. Please enter a number from 1-6.")

if __name__ == "__main__":
    main()


