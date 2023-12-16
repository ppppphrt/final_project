class User:
    def __init__(self, id, firstname, lastname, type):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.type = type

    def __str__(self):
        return f'{self.id} : {self.firstname} {self.lastname} , {self.type}'


from database import DB, Table  # Assuming you have these classes in your database module


class Admin:
    def __init__(self, database):
        self.database = database

    def manage_database(self):
        print("Database Management Menu:")
        print("1. Create Table")
        print("2. Drop Table")
        choice = input("Enter your choice (1/2): ")

        if choice == '1':
            table_name = input("Enter table name: ")
            self.create_table(table_name)
        elif choice == '2':
            table_name = input("Enter table name to drop: ")
            self.drop_table(table_name)
        else:
            print("Invalid choice.")

    def create_table(self, table_name):
        predefined_tables = ['users', 'projects', 'tasks']

        if table_name in predefined_tables:
            print(f"Table '{table_name}' already exists.")
        else:
            new_table = Table(table_name)
            self.database.insert(new_table)
            print(f"Table '{table_name}' created successfully.")

    def drop_table(self, table_name):
        existing_table = self.database.search(table_name)

        if existing_table:
            self.database.database.remove(existing_table)
            print(f"Table '{table_name}' dropped successfully.")
        else:
            print(f"Table '{table_name}' does not exist.")

    def create_user_account(self, user_info):

        users_table = self.database.search('users')
        users_table.insert(user_info)
        self.database.insert(users_table)

    def remove_user_account(self, user_id):

        users_table = self.database.search('users')
        user_to_remove = users_table.find({'id': user_id})
        if user_to_remove:
            users_table.remove(user_to_remove[0])
            self.database.insert(users_table)

    def view_all_projects(self):

        projects_table = self.database.search('projects')
        for project in projects_table.table:
            print(f"Project ID: {project['id']}, Title: {project['title']}, Description: {project['description']}")


class Student:
    def __init__(self, id, firstname, lastname, type, projects=[]):
        self.user = User(id, firstname, lastname, type)
        self.projects = projects

    def join_project(self, project):
        self.projects.append(project)
        project.add_member(self)

    def leave_project(self, project):
        self.projects.remove(project)
        project.remove_member(self)


class LeadStudent:
    def __init__(self, id, firstname, lastname, type, projects=[]):
        self.student = Student(id, firstname, lastname, type, projects)

    def create_project(self, project_id, title, description):
        project = Project(project_id, title, description, self)
        self.student.projects.append(project)
        return project

    def invite_member(self, student, project):
        if student not in project.members:
            project.add_member(student)
            print(f"{student.firstname} {student.lastname} has been invited to join the project '{project.title}'.")

    def remove_member(self, student, project):
        project.remove_member(student)
        print(f"{student.firstname} {student.lastname} has been removed from the project '{project.title}'.")

    def submit_project(self, project):
        project.submitted = True
        print(
            f"Project '{project.title}' has been submitted for review. Advisor: {project.advisor.firstname} {project.advisor.lastname}.")


class MemberStudent:
    def __init__(self, id, firstname, lastname, type, projects=[]):
        self.student = Student(id, firstname, lastname, type, projects)

    def update_project_details(self, project, new_details):
        project.update_details(new_details)


class Faculty:
    def __init__(self, id, firstname, lastname, type, projects_to_evaluate=[]):
        self.user = User(id, firstname, lastname, type)
        self.projects_to_evaluate = projects_to_evaluate

    def evaluate_project(self, project):
        pass

    def assign_project(self, project):
        self.projects_to_evaluate.append(project)


class AdvisingFaculty:
    def __init__(self, id, firstname, lastname, type, projects_to_evaluate=[]):
        self.faculty = Faculty(id, firstname, lastname, type, projects_to_evaluate)

    def approve_project(self, project):
        project.approved = True

    def deny_project(self, project):
        project.approved = False

    def advise_project(self, project):
        pass


class Project:
    def __init__(self, project_id, title, description, lead):
        self.project_id = project_id
        self.title = title
        self.description = description
        self.lead = lead
        self.members = []
        self.advisor = None
        self.submitted = False
        self.approved = False

    def add_member(self, user):
        self.members.append(user)

    def remove_member(self, user):
        self.members.remove(user)

    def set_advisor(self, user):
        self.advisor = user

    def update_details(self, new_details):
        self.title = new_details['title']
        self.description = new_details['description']

    def display_project_details(self):
        print(f"Project ID: {self.project_id}, Title: {self.title}, Description: {self.description}")


admin = Admin()
user = User(2, "Jane", "Smith", "user")
print(user)
