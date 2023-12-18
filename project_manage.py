# import database module
from database import DB, Table
import csv
import os
from run_manage import *

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

# define a funcion called initializing


db = DB()


def initializing():
    # here are things to do in this function:

    # create an object to read all csv files that will serve as a persistent state for this program

    # create all the corresponding tables for those csv files

    # see the guide how many tables are needed

    # add all these tables to the database
    with open('login.csv', mode='r') as f:
        login_data = list(csv.DictReader(f))

    with open('persons.csv', mode='r') as file:
        persons_data = list(csv.DictReader(file))

    with open('project.csv', mode='r') as file:
        project_data = list(csv.DictReader(file))

    with open('Advisor_pending_request.csv', mode='r') as file:
        advice_pending = list(csv.DictReader(file))

    with open('Member_pending_request.csv', mode='r') as file:
        member_pending = list(csv.DictReader(file))

    advice_pending_table = Table('advice_pending', [])
    for row in advice_pending:
        advice_pending_table.insert(row)

    member_pending_table = Table('member_pending', [])
    for row in member_pending:
        member_pending_table.insert(row)

    persons_table = Table('persons', [])
    for row in persons_data:
        persons_table.insert(row)

    project_table = Table('project', [])
    for row in project_data:
        project_table.insert(row)

    db.insert(persons_table)
    db.insert(project_table)
    db.insert(member_pending_table)
    db.insert(advice_pending_table)

    login_table = Table('login', [])
    for login in login_data:
        person_id = login['person_id']
        username = login['username']
        password = login['password']
        role = login['role']
        login_table.insert({'person_id': person_id, 'username': username, 'password': password, 'role': role})
    db.insert(login_table)

    return db


# define a funcion called login

def login(db):
    # here are things to do in this function:
    # add code that performs a login task
    # ask a user for a username and password
    # returns [ID, role] if valid, otherwise returning None
    username = input("Enter username: ")
    password = input("Enter password: ")
    login_table = db.search('login')
    matching_users = login_table.filter(lambda user: user['username'] == username and user['password'] == password)
    if matching_users:
        user = matching_users.table[0]
        return user['person_id'], user['role']
    else:
        return None
        # print(matching_users)


# define a function called exit
def exit(db):
    # here are things to do in this function:
    # write out all the tables that have been modified to the corresponding csv files
    # By now, you know how to read in a csv file and transform it into a list of dictionaries. For this project, you also need to know how to do the reverse, i.e., writing out to a csv file given a list of dictionaries. See the link below for a tutorial on how to do this:

    # https://www.pythonforbeginners.com/basics/list-of-dictionaries-to-csv-in-python

    for table in db.database:
        table_name = table.table_name
        with open(os.path.join(__location__, f'{table_name}.csv'), 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=table.table[0].keys())
            writer.writeheader()
            writer.writerows(table.table)


# make calls to the initializing and login functions defined above

initializing()
val = login(db)

# based on the return value for login, activate the code that performs activities according to the role defined for that person_id

if val[1] == 'admin':
    admin_menu(db)

# see and do admin related activities
elif val[1] == 'student':
    student_menu(db,val[0])

# see and do student related activities
elif val[1] == 'member':
    member_student_menu(db)
# see and do member related activities
elif val[1] == 'lead':
    database = lead_student_menu(db, val[0])
# see and do lead related activities
elif val[1] == 'faculty':
    faculty_menu(db)
# see and do faculty related activities
elif val[1] == 'advisor':
    advising_faculty_menu(db)
# see and do advisor related activities


# once everyhthing is done, make a call to the exit function
exit(db)
