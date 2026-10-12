import json

STUDENT_FILE = "students.json"

def load_students():
    try:
        with open(STUDENT_FILE, "r") as file:
            return json.load(file)

    except FileNotFoundError:
        return []

    except json.JSONDecodeError:
        print("Saved student file has an error.")
        return []


def save_students(student_list):
    with open(STUDENT_FILE, "w") as file:
        json.dump(student_list, file, indent=4)

students = load_students()


TEACHER_FILE = "teachers.json"

def load_teachers():
    try:
        with open(TEACHER_FILE, "r") as file:
            return json.load(file)

    except FileNotFoundError:
        return []

    except json.JSONDecodeError:
        print("Saved teacher file has an error.")
        return []

def save_teachers(teacher_list):
    with open(TEACHER_FILE, "w")as file:
        json.dump(teacher_list, file, indent=4 )


teachers = load_teachers()

CLASS_FILE = "classes.json"

def load_classes():
    try:
        with open(CLASS_FILE, "r") as file:
            return json.load(file)

    except FileNotFoundError:
        return []

    except json.JSONDecodeError:
        print("Saved class file has an error.")
        return []

def save_classes(classes_list):
    with open(CLASS_FILE, "w")as file:
        json.dump(classes_list, file, indent=4 )


classes = load_classes()

SUBJECT_FILE = "subjects.json"

def load_subjects():
    try:
        with open(SUBJECT_FILE, "r") as file:
            return json.load(file)

    except FileNotFoundError:
        return []

    except json.JSONDecodeError:
        print("Saved subject file has an error.")
        return []

def save_subjects(subjects_list):
    with open(SUBJECT_FILE, "w")as file:
        json.dump(subjects_list, file, indent=4 )


subjects = load_subjects()


def print_main_menu():
    print("\n=========================")
    print("SCHOOL MANAGEMENT SYSTEM")
    print("=========================")
    print("1. Manage students")
    print("2. Manage teachers")
    print("3. Manage classes")
    print("4. Manage subjects")
    print("5. View school statistics")
    print("6. Exit")

def print_student_manu():
    print("\n=================")
    print("STUDENT MANAGEMENT")
    print("==================")
    print("1. Add student")
    print("2. View student")
    print("3. Search student")
    print("4. Update student")
    print("5. Delete student")
    print("6. Back to main menu")

def add_student():
    Student_id = input("Student ID: ")
    Name = input("Full name: ")
    Age = input("Age: ")
    Gender = input("Gender: ")
    Student_class = input("Class: ")

    student = {
        "id": Student_id,
        "name": Name,
        "age": Age,
        "gender": Gender,
        "class": Student_class
    }

    students.append(student)
    save_students(students)

    print("student added sucessfully!")

def view_student():
    if len(students) == 0:
        print("No students have been added yet.")
        return
    print("\nALL STUDENTS")

    for student in students:
        print("-------------")
        print("Student ID:", student["id"])
        print("Name:", student["name"])
        print("Age:", student["age"])
        print("Gender:", student["gender"])
        print("Class:", student["class"])

def search_student():
    search_name = input("enter student ID or name to search: ").lower()

    found = False

    for student in students:
        student_id = student["id"].lower()
        student_name = student["name"].lower()

        if search_name == student_id or search_name in student_name:
            print("\n--------------------------")
            print("Student ID :", student["id"])
            print("Name:", student["name"])
            print("Age:", student["age"])
            print("Gender:", student["gender"])
            print("Class:", student["class"])

            found = True

    if found == False:
        print("No student was found.")

def update_student():
    student_id = input("enter Student ID to update: ")

    for student in students:
        if student["id"].lower() == student_id.lower():

            print("\nCurrent student information")
            print("Name:", student["name"])
            print("Age:", student["age"])
            print("Gender:", student["gender"])
            print("Class:", student["class"])

            print("\nEnter the new information")

            student["name"] = input("New name: ")
            student["age"] = input("New age: ")
            student["gender"] = input("New gender: ")
            student["class"] = input("New class: ")

            save_students(students)

            print("Student updated successfully!")
            return

def delete_student():
    Student_id = input("enter student ID to delete: ")

    for student in students:
        if student["id"].lower() == Student_id.lower():
            confirmation = input(
                f"Delete {student['name']}? Type yes to confirm: "
            ).lower()

            if confirmation == "yes":
                students.remove(student)
                save_students(students)
                print("Student deleted successfully!")

            else:
                print("Deletion cancelled.")

            return

def manage_students():
    while True:
        print_student_manu()

        choice = input("choose an option (1-6): ")

        if choice == "1":
            add_student()

        elif choice == "2":
            view_student()

        elif choice == "3":
            search_student()

        elif choice == "4":
            update_student()

        elif choice == "5":
            delete_student()

        elif choice == "6":
            break

        else:
            print("that student option is not ready yet.")

def print_teacher_menu():
    print("\n=========================")
    print("TEACHER MANAGEMENT")
    print("=========================")
    print("1. Add teacher")
    print("2. View teachers")
    print("3. Search teacher")
    print("4. Update teacher")
    print("5. Delete teacher")
    print("6. Back to main menu")

def add_teachers():
    teacher_id = input("teacher ID: ")
    name = input("name: ")
    subject = input("subject taught: ")
    phone = input("phone number: ")

    teacher = {
        "id": teacher_id,
        "name": name,
        "subject": subject,
        "phone": phone
    }

    teachers.append(teacher)
    save_teachers(teachers)


    print("teacher added sucessfully!")

def view_teachers():
    if len(teachers) == 0:
        print("no teacher have added yet.")
        return

    print("\nALL TEACHERS")

    for teacher in teachers:
        print("--------------")
        print("Teacher ID:", teacher["id"])
        print("Name:", teacher["name"])
        print("Subject:", teacher["subject"])
        print("phone:", teacher["phone"])

def search_teacher():
    search_word= input("enter teacher name to search: ").lower()

    found = False

    for teacher in teachers:
        teacher_id = teacher["id"].lower()
        teacher_name = teacher["name"].lower()

        if search_word == teacher_id or search_word in teacher_name:
            print("\n--------------------------")
            print("Teacher ID :", teacher["id"])
            print("Name:", teacher["name"])
            print("subject:", teacher["subject"])
            print("phone number:", teacher["phone"])

            found = True

    if found == False:
        print("No teacher was found.")


def update_teacher():
    teacher_id = input("enter teacher ID to update: ")

    for teacher in teachers:
        if teacher["id"].lower() == teacher_id.lower():
            
            print("\nCurrent student information")
            print("teacher:", teacher["id"])
            print("name:", teacher["name"])
            print("subject:", teacher["subject"])
            print("phone:", teacher["phone"])

            print("\nEnter the new information")

            teacher["teacher"] = input("New teacher: ")
            teacher["name"] = input("New name: ")
            teacher["subject"] = input("New subject: ")
            teacher["phone"] = input("New phone: ")

            save_teachers(teachers)

            print("Student updated successfully!")
            return

def delete_teacher():
    teacher_id = input("enter teacher ID to delete: ")

    for teacher in teachers:
        if teacher["id"].lower() == teacher_id.lower():
            confirmation = input(
                f"Delete {teacher['name']}? Type yes to confirm: "
            ).lower()

            if confirmation == "yes":
                teachers.remove(teacher)
                save_teachers(teachers)
                print("teacher deleted successfully!")

            else:
                print("Deletion cancelled.")
                return
                
def manage_teachers():
    while True:
        print_teacher_menu()

        choice = input("Choose an option (1-6): ")

        if choice == "1":
            add_teachers()

        elif choice == "2":
            view_teachers()

        elif choice == "3":
            search_teacher()

        elif choice == "4":
            update_teacher()

        elif choice == "5":
            delete_teacher()

        elif choice == "6":
            break

        else:
            print("That teacher option is not ready yet.")

def print_class_manu():
    print("\n=================")
    print("CLASS MANAGEMENT")
    print("==================")
    print("1. Add class")
    print("2. View class")
    print("3. Search class")
    print("4. Update class")
    print("5. Delete class")
    print("6. Back to main menu")

def add_classes():
    class_name = input("class name: ")
    class_arm = input("class arm: ")
    assigned_teacher= input("assigned teacher: ")

    class_data = {
        "name": class_name,
        "arm": class_arm,
        "assigned_teacher": assigned_teacher
    }

    classes.append(class_data)
    save_classes(classes)

    print("class added sucessfully!")

def view_classes():
    if len(classes) == 0:
        print("no classes have been added yet.")
        return

    print("\nALL CLASSES")

    for class_data in classes:
        print("--------------")
        print("Class name:", class_data["name"])
        print("Arm:", class_data["arm"])
        print("Assigned teacher:", class_data.get("assigned_teacher"))
        

def search_class():
    search_word= input("enter class name to search: ").lower()

    found = False

    for class_data in classes:
        class_name = class_data["name"].lower()
        arm = class_data["arm"].lower()

        if search_word == class_name or search_word in arm:
            print("\n--------------------------")
            print("Class_name:", class_data.get("class_name"))
            print("Arm:", class_data["arm"])
            print("Assigned_teacher:", class_data["assigned_teacher"])

            found = True

    if found == False:
        print("No class was found.")

def update_class():
    class_name = input("enter class to update: ")

    for class_data in classes:
        if class_name.lower() == class_name.lower():
            
            print("\nCurrent student information")
            print("class_name:", class_data["class data"])
            print("class_arm:", class_data["class arm"])
            print("assigned teacher:", class_data["assigned teacher"])

            print("\nEnter the new information")

            class_data["teacher"] = input("New class name: ")
            class_data["class_arm"] = input("New class arm: ")
            class_data["assigned_teacher"] = input("New assigned teacher: ")

            save_classes(classes)

            print("class updated successfully!")
            return

def delete_class():
    class_name = input("enter class name to delete: ")

    for class_data in classes:
        if class_data["name"].lower() == class_name.lower():
            confirmation = input(
                f"Delete {class_data['name']}? Type yes to confirm: "
            ).lower()

            if confirmation == "yes":
                classes.remove(class_data)
                save_classes(classes)
                print("class deleted successfully!")

            else:
                print("Deletion cancelled.")
            return

def manage_classes():
    while True:
        print_class_manu()

        choice = input("Choose an option (1-6): ")

        if choice == "1":
            add_classes()

        elif choice == "2":
            view_classes()

        elif choice == "3":
            search_class()

        elif choice == "4":
            update_class()

        elif choice == "5":
            delete_class()

        elif choice == "6":
            break

        else:
            print("that class option is not ready yet.")

def print_subjects_manu():
    print("\n=================")
    print("SUBJECT MANAGEMENT")
    print("==================")
    print("1. Add subject")
    print("2. View subject")
    print("3. update subject")
    print("4. Search subject")
    print("5. Delete subject")
    print("6. Back to main manu")

def add_subjects():
    subject_name = input("subject_name: ")
    subject_code = input("subject_code: ")
    teacher= input("teacher: ")

    subject = {
        "name": subject_name,
        "code": subject_code,
        "teacher": teacher
    }

    subjects.append(subject)
    save_subjects(subjects)

    print("subject added sucessfully!")

def view_subjects():
    if len(subjects) == 0:
        print("no subjects have been added yet.")
        return

    print("\nALL SUBJECTS")

    for subject in subjects:
        print("--------------")
        print("Subject_name:", subject.get("name"))
        print("class_code:", subject["code"])
        print("teacher:", subject.get("teacher"))
        

def search_subject():
    search_word= input("enter subject name to search: ").lower()

    found = False

    for subject in subjects:
        subject_name = subject["name"].lower()
        subject_code = subject["code"].lower()

        if search_word == subject_name or search_word in subject_code:
            print("\n--------------------------")
            print("Subject_name:", subject.get("subject_name"))
            print("Subject_code:", subject["code"])
            print("Teacher:", subject.get("teacher"))

            found = True

    if found == False:
        print("No subject was found.")

def update_subject():
    subject_code = input("enter subject code to update: ")

    for subject in subjects:
        if subject["code"].lower() == subject_code.lower():
            

            print("\nCurrent student information")
            print("Name:", subject["name"])
            print("code:", subject["code"])
            print("teacher:", subject["teacher"])

            print("\nEnter the new information")

            subject["name"] = input("New name: ")
            subject["code"] = input("New code: ")
            subject["teacher"] = input("New teacher: ")

            save_subjects(subjects)

            print("Subject updated successfully!")
            return

def delete_subject():
    subject_code = input("enter subject code to delete: ")

    for subject in subjects:
        if subject["code"].lower() == subject_code.lower():
            confirmation = input(
                f"Delete {subject['name']}? Type yes to confirm: "
            ).lower()

            if confirmation == "yes":
                subjects.remove(subject)
                save_subjects(subjects)
                print("subject deleted successfully!")

            else:
                print("Deletion cancelled.")
            return

def manage_subjects():
    while True:
        print_subjects_manu()

        choice = input("enter an option(1-6): ")

        if choice == "1":
            add_subjects()

        elif choice == "2":
            view_subjects()

        elif choice == "3":
            search_subject()

        elif choice == "4":
            update_subject()

        elif choice == "5":
            delete_subject()

        elif choice == "6":
            break

        else:
            print("invalid subject option. please choose 1-6.")

def view_school_statistics():
    print("\n===============")
    print("SHOOL STATISTICS")
    print("================")

    total_students = len(students)
    total_teachers = len(teachers)
    total_classes = len(classes)
    total_students = len(subjects)

    print("total students:", total_students)
    print("total teachers:", total_teachers)
    print("total classes:", total_classes)
    print("total subjects:", total_students)

while True:
        print_main_menu()

        choice = input("enter an option(1-6): ")

        if choice == "1":
            manage_students()

        elif choice == "2":
            manage_teachers()

        elif choice == "3":
            manage_classes()

        elif choice == "4":
            manage_subjects()

        elif choice == "5":
            view_school_statistics()

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("that option is not ready yet.")