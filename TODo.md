1. User 
   - Attributes:
     - id, firstname, lastname, type
   - Methods:
     - __init__(self, id, firstname, lastname, type): Initialize the user with ID, firstname,lastname and type

2. Admin 
   - Methods:
     - manage_database(self): Implement code to manage database operations 
     - create_user_account(self, user_info): Create a new user account. The user_info parameter contains necessary user details.
     - remove_user_account(self, user_id): Remove a user account based on the given user_id.
     - view_all_projects(self): Implement a method to view details of all projects in the system.

3. Student 
   - Attributes:
     - projects: A list of projects the student is involved in.
   - Methods:
     - join_project(self, project): Add the student to a project's member list and add the project to the student's projects list.
     - leave_project(self, project): Remove the student from a project's member list and remove the project from the student's projects list.

4. LeadStudent 
   - Methods:
     - create_project(self, project_id, title, description): Create a new project with the given details and add it to the student's project list.
     - invite_member(self, student, project): Send an invitation to a student to join a project.
     - remove_member(self, student, project): Remove a student from a project.
     - submit_project(self, project): Submit the final report or completion of the project.

5. MemberStudent 
   - Methods:
     - update_project_details(self, project, new_details): Allow a member student to propose updates to project details.

6. Faculty 
   - Attributes:
     - projects_to_evaluate: Projects assigned for evaluation.
   - Methods:
     - evaluate_project(self, project): Implement the evaluation logic for a project.
     - assign_project(self, project): Assign a project to this faculty member for evaluation.

7. AdvisingFaculty 
   - Additional Methods:
     - approve_project(self, project): Approve a project.
     - deny_project(self, project): Deny approval for a project.
     - advise_project(self, project): Provide advice and guidance for a project.

8. Project 
   - Attributes:
     - project_id, title, description, lead, members, advisor
   - Methods:
     - add_member(self, user): Add a user to the project's member list.
     - remove_member(self, user): Remove a user from the project's member list.
     - set_advisor(self, user): Set a faculty member as the project advisor.
     - update_details(self, new_title, new_description): Update the project's title and description.
     - display_project_details(self): Display the details of the project.
