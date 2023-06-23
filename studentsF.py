import csv
import sys

student_fields = ["idNum", "firstName", "lastName", "course"]
course_fields = ["courseCode", "courseName"]


def action():
    print("\nPress any key to return to menu")
    print("Select 0 to exit")
    answer = input("Select: ")

    if answer == '0':
        sys.exit(0)
    else:
        main()


def find_course(course):
    is_found = False
    courses = []
    with open("courses.csv", "r") as courses_file:
        reader = csv.DictReader(courses_file, fieldnames=course_fields)
        for row in reader:
            if course.lower() in [x.lower() for x in row.values()]:
                is_found = True
                courses.append[row]

    return is_found, courses


def find_student(student):
    is_found = False
    students = []
    with open("students.csv", "r") as students_file:
        reader = csv.DictReader(students_file, fieldnames=student_fields)
        for row in reader:
            if student.lower() in [x.lower() for x in row.values()]:
                is_found = True
                students.append(row)

    return is_found, students


def find_id(key, csv_file):
    with open(csv_file, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == key:
                return True

    return False


def change(key, value, field, csv_file):
    field = int(field) - 1
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        rows = list(reader)
        for row in rows:
            if key in row:
                row[field] = value

    with open(csv_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)
        print("\nUpdate Successful")


def view():
    print("\n1. View Students")
    print("2. View Courses")
    answer = input("Select: ")

    if answer == '1':
        view_student()
    elif answer == '2':
        view_course()
    else:
        print("\nSelected value is invalid")
        return


def view_student():
    with open("students.csv", "r") as students_file:
        reader = csv.DictReader(students_file, fieldnames=student_fields)
        print("\nID Number, Last Name, First Name, Course Code")
        next(reader)
        for row in reader:
            id_number = row["idNum"]
            first_name = row["firstName"]
            last_name = row["lastName"]
            course = row["course"]
            print(f"{id_number}, {first_name}, {last_name}, {course}")


def view_course():
    with open("courses.csv", "r") as courses_file:
        reader = csv.DictReader(courses_file, fieldnames=course_fields)
        print("\nCourse Code - Course Name")
        next(reader)
        for row in reader:
            course_code = row["courseCode"]
            course_name = row["courseName"]
            print(f"{course_code} - {course_name}")


def search():
    print("\n1. Search Student")
    print("2. Search Course")
    answer = input("Select: ")

    if answer == '1':
        print("\nSearch student by First Name, Last Name or ID Number")
        student = input("Search: ")
        search_student(student)
    elif answer == '2':
        print("\nSearch Course by Course ID or Course Name")
        course = input("Search: ")
        search_course(course)
    else:
        print("\nSelected Value is Invalid")


def search_student(student):
    is_found, students = find_student(student)
    if not is_found:
        print("\nStudent does not exist")
        print("Add New Student? (y/n)")
        answer = input("Select: ")
        if answer.lower() == 'y':
            add_student()
        elif answer.lower() == 'n':
            print("\nNo new student is added")
            action()
        else:
            print("\nSelected value is invalid")
            action()

    for index in students:
        id_number = index["idNum"]
        first_name = index["firstName"]
        last_name = index["lastName"]
        course = index["course"]

        print(f"\nName: {first_name}, {last_name}")
        print(f"ID Number: {id_number}")
        print(f"Course: {course}")


def search_course(course):
    is_found, courses = find_course(course)
    if not is_found:
        print("\nCourse does not exist")
        print("Add New Course? (y/n)")
        answer = input("Select: ")
        if answer.lower() == 'y':
            add_course()
        elif answer.lower() == 'n':
            print("\nNo new course is added")
            action()
        else:
            print("Selected value is invalid")
            action()

    for index in course:
        course_code = index["courseCode"]
        course_name = index["courseName"]
        print(f"\n{course_code} - {course_name}")


def add():
    print("\n1. Add New Student")
    print("2. Add New Course")
    answer = input("Select: ")

    if answer == '1':
        add_student()
    elif answer == '2':
        add_course()
    else:
        print("\nSelected value is invalid")
        return


def add_course():
    print("\nEnter New Course")
    course_id = input("Course ID: ")
    course_id = course_id.upper()
    course_name = input("Course Name: ")

    with open("courses.csv", "r") as course_file:
        reader = csv.reader(course_file)
        for row in reader:
            if course_id in row:
                print("Course ID already exists")
                action()

    with open("courses.csv", "a", newline='') as courses_file:
        writer = csv.writer(courses_file)
        writer.writerow([course_id, course_name])
        print("\nCourse Added")
        return


def add_student():
    print("\nEnter New Student Info")
    id_number = input("ID number: ")
    with open("students.csv", "r") as student_file:
        reader = csv.reader(student_file)
        for row in reader:
            if id_number in row:
                print("Student ID already exists")
                return

    first_name = input("First Name: ")
    last_name = input("Last Name: ")

    course = input("Course Code: ")
    course = course.upper()

    is_found, courses = find_course(course)
    if not is_found:
        print("\nCourse ID does not exist")
        print("Please add new course before adding new student")
        return

    with open("students.csv", "a", newline='') as students_file:
        writer = csv.writer(students_file)
        writer.writerow([id_number, first_name, last_name, course])
        print("\nStudent added")

    search_student(id_number)


def edit():
    print("\n1. Edit Student")
    print("2. Edit Courses")
    answer = input("Select: ")

    if answer == '1':
        student_id = input("\nEnter ID Number of student: ")
        edit_student(student_id)
    elif answer == '2':
        course_id = input("\nEnter course Code: ")
        edit_course(course_id)
    else:
        print("Selected value is invalid")


def edit_student(student_id):
    is_found = find_id(student_id, "students.csv")
    if not is_found:
        print("\nNo matches found")
        return

    search_student(student_id)

    print("\nEdit student information by:")
    print(" 1. ID Number")
    print(" 2. First Name")
    print(" 3. Last Name")
    print(" 4. Course")
    print(" 5. Delete Student")
    print(" Select 0 to exit")
    field = input("\nSelect: ")

    update = ' '
    if field == '1':
        update = input("Edit ID Number: ")
        is_found, students = find_student(update)
        if is_found:
            print("\nThis student ID is already taken")
            return

    elif field == '2':
        update = input("Edit First Name: ")
    elif field == '3':
        update = input("Edit Last Name: ")

    elif field == '4':
        update = input("Edit Course: ")
        is_found, courses = find_course(update)
        if not is_found:
            print("\nCourse ID does not exist")
            return

    elif field == '5':
        confirm_del(student_id, "students.csv")
        return

    elif field == '0':
        sys.exit(0)

    else:
        print("Number selected is invalid")
        return

    change(student_id, update, field, "students.csv")
    search_student(update)


def edit_course(course_id):
    course_id = course_id.upper()
    search_course(course_id)

    print("\nEdit course by")
    print("1. Course Code")
    print("2. Course Name")
    print("3. Delete Course")
    field = input("Select: ")

    if field == '1':
        update = input("\nEdit Course Code: ")
    elif field == '2':
        update = input("\nEdit Course Name: ")
    elif field == '3':
        delete_course(course_id)
        return
    else:
        print("Selected value is invalid")
        return

    change(course_id, update, field, "courses.csv")
    print("\nUpdate Successful")
    search_course(update)


def delete_course(course_code):
    # Find the course
    is_found, courses = find_course(course_code)
    if not is_found:
        print("\nCourse does not exist")
        return

    # Delete the course
    confirm_del(course_code, "courses.csv")

    # Delete all students under the course
    del_count = 0
    with open("students.csv", "r", newline='') as file:
        reader = csv.reader(file)
        students = list(reader)
        for student in students:
            if course_code.upper() in student:  # Check if student is under the course
                delete(student[0], "students.csv")  # Delete the student
                del_count += 1

    if del_count > 0:
        print(f"Deleted {del_count} students under course")
    else:
        print("\nNo students found under the course.")


def confirm_del(key, csv_file):
    print("\nConfirm Action")
    print("Select 1 to delete")
    print("Select any key to cancel")
    answer = input("Select: ")

    if answer != '1':
        print("\nCancelled")
        action()
    delete(key, csv_file)


def delete(key, csv_file):
    keep = []

    with open(csv_file, "r", newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if key.lower() not in [x.lower() for x in row.values()]:
                keep.append(row)

    with open(csv_file, "w", newline='') as file:
        writer = csv.DictWriter(file, fieldnames=reader.fieldnames)
        writer.writeheader()
        writer.writerows(keep)

    print("\nDeleted")


def main():
    print("\nSelect an option")
    print(" 1. View")
    print(" 2. Search")
    print(" 3. Add")
    print(" 4. Edit")
    print(" Select 0 to exit")

    answer = input("\nSelect: ")

    if answer == '1':
        view()
    elif answer == '2':
        search()
    elif answer == '3':
        add()
    elif answer == '4':
        edit()
    elif answer == '0':
        sys.exit(0)

    action()


main()
