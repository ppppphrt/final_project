from test import LeadStudent, Student, Faculty, DB, Admin


def create_lead_student():
    id = input("Enter student ID: ")
    firstname = input("Enter student firstname: ")
    lastname = input("Enter student lastname: ")
    type = "lead_student"

    return LeadStudent(id, firstname, lastname, type)


def create_student():
    id = input("Enter student ID: ")
    firstname = input("Enter student firstname: ")
    lastname = input("Enter student lastname: ")
    type = "student"

    return Student(id, firstname, lastname, type)


def create_faculty_member():
    id = input("Enter faculty ID: ")
    firstname = input("Enter faculty firstname: ")
    lastname = input("Enter faculty lastname: ")
    type = "faculty"

    return Faculty(id, firstname, lastname, type)


def admin_menu(database):
    admin = Admin(database)
    while True:
        print("\nAdmin Menu:")
        print("1. Manage Database")
        print("2. Exit to Main Menu")

        admin_choice = input("Enter your choice (1/2): ")

        if admin_choice == '1':
            admin.manage_database()
        elif admin_choice == '2':
            print("Returning to main menu.")
            break
        else:
            print("Invalid choice. Please enter a valid number.")


def lead_student_menu():
    lead_student = create_lead_student()
    project = lead_student.create_project('project_id', 'title', 'description')
    while True:
        print("\nLead Student Menu:")
        print("1. Create Project")
        print("2. Invite Member to Project")
        print("3. Remove Member from Project")
        print("4. Submit Project for Review")
        print("5. Exit to Main Menu")

        lead_student_choice = input("Enter your choice (1/5): ")

        if lead_student_choice == '1':
            lead_student.create_project('project_id', 'title', 'description')
        elif lead_student_choice == '2':
            lead_student.invite_member(project)  # TODO: Add Request to Member too
        elif lead_student_choice == '3':
            lead_student.remove_member(project)
        elif lead_student_choice == '4':
            lead_student.submit_project(project)  # TODO: Change Response Status in Request Pending Member in Table
        elif lead_student_choice == '5':
            print("Returning to main menu.")
            break
        else:
            print("Invalid choice. Please enter a valid number.")


def func():
    id = input("Enter student ID: ")
    firstname = input("Enter student firstname: ")
    lastname = input("Enter student lastname: ")
    type = "lead_student"

    return LeadStudent(id, firstname, lastname, type), Student(id, firstname, lastname, type), Faculty(id, firstname, lastname, type)


def student_menu():
    # lead_student = create_lead_student(admin)
    lead_student, student, faculty = func()
    project = lead_student.create_project('project_id', 'title', 'description')

    # student = create_student()
    join_project = student.join_project
    leave_project = student.leave_project
    while True:
        print("\nRegular Student Menu:")
        print("1. Join Project")
        print("2. Leave Project")
        print("3. Exit to Main Menu")

        student_choice = input("Enter your choice (1/3): ")

        if student_choice == '1':
            join_project(project)
        elif student_choice == '2':
            leave_project(project)
        elif student_choice == '3':
            print("Returning to main menu.")
            break
        else:
            print("Invalid choice. Please enter a valid number.")


def faculty_menu():
    lead_student, student , faculty_member = func()
    project = lead_student.create_project('project_id', 'title', 'description')

    # faculty_member = create_faculty_member()
    evaluate_project = faculty_member.evaluate_project
    advise_project = faculty_member.assign_project

    while True:
        print("\nFaculty Menu:")
        print("1. Evaluate Project")
        print("2. Advise Project")
        print("3. Exit to Main Menu")

        faculty_choice = input("Enter your choice (1/3): ")

        if faculty_choice == '1':
            evaluate_project(project)
        elif faculty_choice == '2':
            advise_project(project)
        elif faculty_choice == '3':
            print("Returning to main menu.")
            break
        else:
            print("Invalid choice. Please enter a valid number.")


def main():
    database_instance = DB()
    admin = Admin(database_instance)

    print("Welcome to the Project Management System!")

    while True:
        print("\nChoose a role:")
        print("1. Admin")
        print("2. Lead Student")
        print("3. Regular Student")
        print("4. Faculty")
        print("5. Exit")

        role_choice = input("Enter the number corresponding to your role: ")

        if role_choice == '1':
            admin_menu(admin)
        elif role_choice == '2':
            lead_student_menu()
        elif role_choice == '3':
            student_menu()
        elif role_choice == '4':
            faculty_menu()
        elif role_choice == '5':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid number.")


if __name__ == "__main__":
    main()

