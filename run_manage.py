from mange import LeadStudent, Student, Faculty, DB, Admin, MemberStudent, AdvisingFaculty


def create_lead_student():
    # id = input("Enter student ID: ")
    # firstname = input("Enter student firstname: ")
    # lastname = input("Enter student lastname: ")
    type = "lead_student"

    return LeadStudent(type)


def create_student():
    # id = input("Enter student ID: ")
    # firstname = input("Enter student firstname: ")
    # lastname = input("Enter student lastname: ")
    type = "student"

    return Student(type)


def create_faculty_member():
    # id = input("Enter faculty ID: ")
    # firstname = input("Enter faculty firstname: ")
    # lastname = input("Enter faculty lastname: ")
    type = "faculty"

    return Faculty(type)


def admin_menu(database):
    admin = Admin(database)
    while True:
        print("\nAdmin Menu")
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


def lead_student_menu(database, lead_id):
    lead_student = create_lead_student()
    project = database.search('project')

    while True:
        print("\nLead Student Menu")
        print("1. Create Project")
        print("2. Invite Member to Project")
        print("3. Remove Member from Project")
        print("4. Submit Project for Review")
        print("5. Exit to Main Menu")

        lead_student_choice = input("Enter your choice (1/5): ")

        if lead_student_choice == '1':
            project_id = input("Enter project ID: ")
            title = input("Enter project title: ")
            project.insert(entry={'ID': project_id, 'Title': title, 'Lead': '', 'Member1': '',
                                  'Member2': '', 'Advisor': '', 'Status': 'In Progress'})
        elif lead_student_choice == '2':
            member_name = input("Enter member's name: ")
            project = lead_student.invite_member(project, member_name)
        elif lead_student_choice == '3':
            member_name = input("Enter member's name to remove: ")
            project = lead_student.remove_member(project, member_name)
        elif lead_student_choice == '4':
            project = lead_student.submit_project(project, lead_id, database.search('persons'))
        elif lead_student_choice == '5':
            print("Returning to main menu.")
            break
        else:
            print("Invalid choice. Please enter a valid number.")

    database.insert(project)
    return database


def member_student_menu(database):
    # member_student_id = input("Enter your ID: ")
    # member_student_firstname = input("Enter your first name: ")
    # member_student_lastname = input("Enter your last name: ")
    member_student_type = input("Enter your type: ")
    # print(database.search('member_pending'))
    member_student = MemberStudent(member_student_type,database.search('member_pending'))

    while True:
        print("\nMember Student Menu")
        print("1. Update Project Details")
        print("2. View Projects")
        print("3. Exit to Main Menu")

        member_student_choice = input("Enter your choice (1/3): ")

        if member_student_choice == '1':
            project_id = input("Enter the project ID: ")
            new_details = input("Enter the new project details: ")
            project = member_student.get_project_by_id(project_id)
            if project:
                member_student.update_project_details(project, new_details,member_student)

            else:
                print(f"Project with ID {project_id} not found.")
        elif member_student_choice == '2':
            project_id = input("Enter the project ID to view: ")
            project = member_student.get_project_by_id(project_id)
            if project:
                member_student.view_project(project,member_student)
            else:
                print(f"Project with ID {project_id} not found.")
        elif member_student_choice == '3':
            print("Returning to main menu.")
            break
        else:
            print("Invalid choice. Please enter a valid number.")


def advising_faculty_menu(database: DB):
    # advising_faculty_id = input("Enter your ID: ")
    # advising_faculty_firstname = input("Enter your first name: ")
    # advising_faculty_lastname = input("Enter your last name: ")
    advising_faculty_type = input("Enter your type: ")

    project_table = database.search('project')

    advising_faculty = AdvisingFaculty(advising_faculty_type, project_table)

    while True:
        print("\nAdvising Faculty Menu")
        print("1. Approve Project")
        print("2. Deny Project")
        print("3. Advise Project")
        print("4. Exit to Main Menu")

        faculty_choice = input("Enter your choice (1/4): ")

        if faculty_choice == '1':
            project_id = input("Enter the project ID to approve: ")
            project = advising_faculty.faculty.get_project_by_id(project_id)
            advising_faculty.approve_project(project,project_id)
            print(f"Project approved successfully.")
        elif faculty_choice == '2':
            project_id = input("Enter the project ID to deny: ")
            project = advising_faculty.faculty.get_project_by_id(project_id)
            advising_faculty.deny_project(project,project_id)
            print(f"Project denied.")
        elif faculty_choice == '3':
            project_id = input("Enter the project ID to advise: ")
            project = advising_faculty.faculty.get_project_by_id(project_id)
            advising_faculty.advise_project(project)
        elif faculty_choice == '4':
            print("Returning to main menu.")
            break
        else:
            print("Invalid choice. Please enter a valid number.")

def func(database,id):
    # id = input("Enter student ID: ")
    # firstname = input("Enter student firstname: ")
    # lastname = input("Enter student lastname: ")
    type = "lead_student"
    project = database.search('project')
    return LeadStudent(type,project), Student(type,project,id), Faculty(type,project)


def student_menu(database,id):
    # lead_student = create_lead_student(admin)
    lead_student, student, faculty = func(database,id)

    project = lead_student.create_project('project_id', 'title', 'description')
    project_ii = database.search('project')
    # student = create_student()
    join_project = student.join_project
    leave_project = student.leave_project
    update_project = student.update_project
    see_project = student.see_project
    member_pending = database.search('member_pending')
    person_table = database.search('persons')
    while True:
        print("\nRegular Student Menu")
        print("1. Join Project")
        print("2. Leave Project")
        print("3. Update Project")
        print("4. View Project")
        print("5. Create Project")
        print("6. Exit to Main Menu")


        student_choice = input("Enter your choice (1/6): ")

        if student_choice == '1':
            join_project(project,member_pending, person_table)

        elif student_choice == '2':
            # leave_project(project)
            print("Project left successfully.")
        elif student_choice == '3':
            new_title = input("Type new title here: ")
            new_description = input("Your new description: ")
            update_project(project,new_title,new_description)
            print("Project Updated")
        elif student_choice == '4':
            see_project(project)

        elif student_choice == '5':
            project_id = input("Enter project ID: ")
            title = input("Enter project title: ")
            project_ii.insert(entry={'ID': project_id, 'Title': title, 'Lead': '', 'Member1': '',
                                  'Member2': '', 'Advisor': '', 'Status': 'In Progress'})
            print("Project has been created successfully!")
        elif student_choice == '6':
            print("Returning to main menu.")
            break
        else:
            print("Invalid choice. Please enter a valid number.")


def faculty_menu(database):
    lead_student, student, faculty_member = func(database,id)
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


# def main():
#     database_instance = DB()
#     admin = Admin(database_instance)
#
#     print("Welcome to the Project Management System!")
#
#     while True:
#         print("\nChoose a role:")
#         print("1. Admin")
#         print("2. Lead Student")
#         print("3. Regular Student")
#         print("4. Faculty")
#         print("5. Exit")
#
#         role_choice = input("Enter the number corresponding to your role: ")
#
#         if role_choice == '1':
#             admin_menu(admin)
#         elif role_choice == '2':
#             lead_student_menu()
#         elif role_choice == '3':
#             student_menu()
#         elif role_choice == '4':
#             faculty_menu()
#         elif role_choice == '5':
#             print("Exiting the program. Goodbye!")
#             break
#         else:
#             print("Invalid choice. Please enter a valid number.")
#
#
# if __name__ == "__main__":
#     main()

