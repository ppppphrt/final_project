# Final project for 2023's 219114/115 Programming I
*  All files
  - database.py
  - project_manage.py
  - manage.py
  - run_manage.py
  - persons.csv
  - project.csv
  - member_pending.csv
  - advisor_pending.csv
  - login.csv
  - TODO.md
  - Proposal.md

# project_manage.py file

1. **Database Module (`database.py`):**
   - Contains classes (`DB` and `Table`) for basic database functionality.

2. **Initialization Function (`initializing`):**
   - Reads data from CSV files and creates corresponding tables.
   - Inserts data into tables and adds them to the main database.

3. **Login Function (`login`):**
   - Takes a `DB` object, prompts for username and password.
   - Validates credentials against the login table and returns user information.

4. **Exit Function (`exit`):**
   - Writes modified tables back to their respective CSV files.

5. **Menu-Based Logic:**
   - Calls specific functions based on the user's role obtained from login.

6. **Menu Functions (`admin_menu`, `student_menu`, etc.):**
   - Presumably contains logic for role-specific activities.

7. **Script Execution:**
   - Initializes the database, performs user login, and executes role-specific activities.
   - Writes modified data back to CSV files before exiting.

# manage.py
- class of each role located here.
1. **Admin:**
   - Manages the overall database.
   - Creates and drops tables.
   - Can create user accounts and remove them.
   - Manages projects (viewing all projects).

2. **Project:**
   - Represents a project with attributes such as project ID, title, description, members, advisor, submission status, and approval status.
   - Allows adding/removing members, setting an advisor, updating project details, and displaying project details.

3. **Student:**
   - A base class for different types of students (LeadStudent, MemberStudent, Faculty, AdvisingFaculty).
   - Contains common attributes like user type and projects.
   - Has method Join , leave , update and see project.

4. **LeadStudent:**
   - Inherits from Student.
   - Has additional methods for creating projects, inviting/removing members, and submitting projects.

5. **MemberStudent:**
   - Inherits from Student.
   - Has methods for updating project details and viewing project information.

6. **Faculty:**
   - Inherits from Student.
   - Represents a faculty member and includes methods for evaluating and assigning projects.

7. **AdvisingFaculty:**
   - Inherits from LeadStudent.
   - Represents a faculty member with advising responsibilities.
   - Has methods for approving/denying projects and providing advice.

8. **DB (Database) and Table:**
   - Classes for managing the database structure.
   - DB holds a list of tables.
   - Table represents a table in the database and has methods for inserting, searching, and removing entries.

# run_manage.py
- use to run each role from manage.py
1. **LeadStudent:**
   - Represents a lead student in the project management system.
   - Methods include creating projects, inviting and removing members, and submitting projects for review.

2. **Student:**
   - Represents a regular student in the project management system.
   - Methods include joining and leaving projects, updating project details, and viewing projects.

3. **Faculty:**
   - Represents a faculty member in the project management system.
   - Methods include evaluating projects and advising projects.

4. **DB (Database):**
   - Represents a simple database class.
   - It has methods for searching, inserting, and managing data.

5. **Admin:**
   - Represents an admin in the project management system.
   - Methods include managing the database.

6. **MemberStudent:**
   - Represents a member student in the project management system.
   - Methods include updating and viewing project details.

7. **AdvisingFaculty:**
   - Represents an advising faculty member in the project management system.
   - Methods include approving, denying, and advising projects.

8. **func:**
   - A utility function that returns instances of LeadStudent, Student, and Faculty.

9. **student_menu:**
   - Represents the menu and actions for a regular student.
   - Allows joining, leaving, updating, and viewing projects.

10. **faculty_menu:**
    - Represents the menu and actions for a faculty member.
    - Allows evaluating and advising projects.

11. **lead_student_menu:**
    - Represents the menu and actions for a lead student.
    - Allows creating projects, inviting and removing members, and submitting projects for review.

12. **admin_menu:**
    - Represents the menu and actions for an admin.
    - Allows managing the database.

13. **advising_faculty_menu:**
    - Represents the menu and actions for an advising faculty member.
    - Allows approving, denying, and advising projects.

14. **create_lead_student, create_student, create_faculty_member:**
    - Utility functions to create instances of LeadStudent, Student, and Faculty.

# How to run my code 

- Run in file project_manage.py (by pressing run button).
- choose people in each role in login.csv file (for example you choose people in 'student' role program will go to student directly).
- continuous step 2 to every role.

# Table Detailing

<img width="910" alt="final evaluation" src="https://github.com/ppppphrt/final_project/assets/113490397/48e5d37a-6da9-4120-8903-86d1abf07245">


# Bugs and Missing Features

- Leave Project is just show but it does not work.
- Faculty can not see a request to be a supervisor.
