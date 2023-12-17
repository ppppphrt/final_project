import database
import csv
import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))


class User:
    def __init__(self, id, firstname, lastname, type):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.type = type

    def __str__(self):
        return f'{self.id} : {self.firstname} {self.lastname} , {self.type}'


from database import DB, Table


class Admin:
    def __init__(self, database: DB):
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
            new_table = Table(table_name, [])
            self.database.insert(new_table)
            print(f"Table '{table_name}' created successfully.")

    def create_user_account(self, user_info):
        table_name = 'users'
        users_table = self.database.search(table_name)

        if users_table is None:
            users_table = Table(table_name)
            self.database.insert(users_table)
            print(f"Table '{table_name}' created successfully.")

        users_table = self.database.search(table_name)

        users_table.insert(user_info)
        self.database.insert(users_table)

    def drop_table(self, table_name):
        existing_table = self.database.search(table_name)

        if existing_table:
            self.database.database.remove(existing_table)
            print(f"Table '{table_name}' dropped successfully.")
        else:
            print(f"Table '{table_name}' does not exist.")

    def remove_user_account(self, user_id):
        users_table = self.database.search('users')
        user_to_remove = users_table.filter(lambda user: user['id'] == user_id)
        if user_to_remove:
            users_table.remove(user_to_remove[0])
            self.database.insert(users_table)

    def view_all_projects(self):
        projects_table = self.database.search('projects')
        for project in projects_table.table:
            print(
                f"Project ID: {project['project_id']}, Title: {project['title']}, Description: {project['description']}")

    def get_database(self):
        return self.database


class Project:
    def __init__(self, project_id, title, description):
        self.project_id = project_id
        self.title = title
        self.description = description
        # self.lead = lead
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



class Student:
    def __init__(self, id, firstname, lastname, type, projects=[]):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.type = type
        self.projects = projects

    def join_project(self, project):
        self.projects.append(project)
        project.add_member(self)

    def leave_project(self, project):
        self.projects.remove(project)
        project.remove_member(self)

    def update_project(self, project, new_title, new_description):
        project.title = new_title
        project.description = new_description
        print(f"Project '{project.title}' has been updated.")

    def see_project(self, project):
        print(f"Project Title: {project.title}")
        print(f"Project ID: {project.project_id}")
        print(f"Description: {project.description}")
        print(f"Members: {[member.fullname() for member in project.members]}")
        print(f"Submitted: {project.submitted}")


class LeadStudent(Student):
    def __init__(self, id, firstname, lastname, type, projects=[]):
        super().__init__(id, firstname, lastname, type, projects)

    def create_project(self, project_id, title, description):
        project = Project(project_id, title, description)
        self.projects.append(project)
        return project

    def invite_member(self, projects, member):
        for project in projects.table:
            if '' in project.values():
                project.update(
                    key=project['ID'],
                    column='Member1',
                    value=member
                )
                # project.add_member(self)
                print(f"{member} has been invited to join the project '{project['Title']}'.")

        return projects

    def remove_member(self, project, member):
        for project in project.table:
            if member in project.values():
                # project.remove_member(self)
                project.update(
                    key=project['ID'],
                    column='Member1',
                    value=''
                )
                print(f"{member} has been removed from the project '{project['Title']}'.")

        return project

    def submit_project(self, projects: Table, lead_id, persons: Table):
        lead = ""
        for person in persons.table:
            if person['ID'] == lead_id:
                lead = person['first'] + " " + person['last']

        is_found = False
        for project in projects.table:
            if project['Status'] == 'Completed' and lead == project['Lead']:
                project.update(
                    key=project['ID'],
                    column='Status',
                    value='Submitted'
                )
                is_found = True
                print(f"Project '{project['Title']}' has been submitted for review.")

        if not is_found:
            print("No project found to submit.")
        return projects


class MemberStudent(Student):
    def __init__(self, id, firstname, lastname, type, projects=[]):
        super().__init__(id, firstname, lastname, type, projects)

    def update_project_details(self, project, new_details):
        project.update_details(new_details)

    def view_project(self, project):
        print(f"Project ID: {project.project_id}")
        print(f"Title: {project.title}")
        print(f"Description: {project.description}")
        print(f"Status: {project.status}")
        print("Members:")
        for member in project.members:
            print(f"- {member.firstname} {member.lastname}")
        print("")

    def get_project_by_id(self, project_id):
        for project in self.projects:
            if project.project_id == project_id:
                return project
        return None



class Faculty:
    def __init__(self, id, firstname, lastname, type, projects_to_evaluate=[]):
        self.user = User(id, firstname, lastname, type)
        self.projects_to_evaluate = projects_to_evaluate

    def evaluate_project(self, project):
        evaluation_result = True

        if evaluation_result:
            project.approved = True
            print(f"Project '{project.title}' has been approved by {self.user.firstname} {self.user.lastname}.")
        else:
            project.approved = False
            print(f"Project '{project.title}' has been denied approval by {self.user.firstname} {self.user.lastname}.")

    def assign_project(self, project):
        self.projects_to_evaluate.append(project)


class AdvisingFaculty(LeadStudent):
    def __init__(self, id, firstname, lastname, type, projects_to_evaluate=[]):
        super().__init__(id, firstname, lastname, type)
        self.faculty = Faculty(id, firstname, lastname, type, projects_to_evaluate)

    def approve_project(self, project):
        project.approved = True

    def deny_project(self, project):
        project.approved = False

    def advise_project(self, project):
        feedback = input("Project Advice: ")
        print(f"Advice for '{project.title}': {feedback}")
