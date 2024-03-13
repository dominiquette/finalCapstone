# Notes:
# 1. Use the following username and password to access the admin rights
# username: admin
# password: password
# 2. Ensure you open the whole folder for this task in VS Code otherwise the
# program will look in your root directory for the text files.

#===== Importing Libraries ===========
import os
from datetime import datetime

# Define the format string for date and time
DATETIME_STRING_FORMAT = "%d-%m-%Y"

#===== Functions ===========

def read_task_file():
    """
    Reads task details from a text file named 'tasks.txt' and returns a list of dictionaries.

    Each dictionary represents a task with attributes like username, title, description, 
    due date, assigned date, and completion status.
    """
    with open("tasks.txt", "r", encoding="utf-8") as file:
        tasks = []
        for line in file:
            # Splitting the line into different attributes based on the comma separator
            line_split = line.strip().split(",")
            
            # Check if the line has the expected number of elements
            if len(line_split) == 6:
                user_dict = {
                    "username": line_split[0],
                    "title": line_split[1],
                    "description": line_split[2],
                    "due_date": datetime.strptime(line_split[3], "%d-%m-%Y"),
                    "assigned_date": datetime.strptime(line_split[4], "%d-%m-%Y"),
                    "completed": line_split[5] == "Yes"
                }
                tasks.append(user_dict)
            else:
                # Print a warning and skip the line if the format is unexpected
                print(f"Warning: Skipping line due to unexpected format: {line}")

        return tasks


def reg_user():
    """
    Registers a new user by prompting for a new username and password.
    This function also checks if the username already exists, prompts for a new password, 
    and adds the new user to the 'user.txt' file if the password is confirmed.
    """
    print("_" * 80)
    print("\n\t\t\033[4mREGISTER A NEW USER\033[0m")
    print()
    while True:
        # Prompt for new username
        new_username = input("\nNew Username:\t\t ")

        # Check if the username already exist
        if not new_username or new_username in username_password:
            print("\nSorry, username already in use. Please enter a unique username ")
        else:
            break

    while True: 
        # Prompt for a new password
        new_password = input("\nNew Password:\t\t ")
        
        # Check if the password is empty
        if not new_password:
            print("Invalid password. Please enter a non-empty password.")
        else:
            confirm_password = input("Confirm Password:\t ")

            # Check if the new password and confirmed password are the same.
            if new_password == confirm_password:
                # Add the new user to the user.txt file (overwriting existing contents)
                print(f"\n\033[1m{new_username}\033[0m has been added as a new user.")
                print("_" * 80)
                username_password[new_username] = new_password
                   
                with open("user.txt", "w", encoding="utf-8") as out_file:
                    # Prepare data for writing to the user.txt file
                    user_data_list = [f"{key};{value}" for key, value in username_password.items()]
                    out_file.write("\n".join(user_data_list)) 
                break
            else:
                print("\nPasswords do no match.")


def add_task():
    """
    The `add_task` function prompts the user to input details of a task, validates the input,
    and adds the task to a list and a text file.

    Input:
    - User assigned to the task
    - Title of the task
    - Description of the task
    - Due date of the task (in DD-MM-YYYY format)

    Output:
    - Updates the task_list and tasks.txt file with the new task information.

    Raises:
    - ValueError: If the due date input is not in the specified DD-MM-YYYY format.
    """

    print("_" * 80)
    print("\n\t\t\033[4mADD A TASK\033[0m")
    print()

    # Get the username for the task
    while True:
        task_username = input("\nUser assigned to task:\t\t ")
        if task_username in username_password:
            break
        print("\nUser does not exist. Please enter a valid username")

    # Get the title for the task
    while True:
        task_title = input("Title of Task:\t\t\t ")
        if not task_title:
            print("\nPlease enter a title for the task.\n")
            continue
        else:
            break
    
    # Get the description for the task
    while True:
        task_description = input("Description of Task:\t\t ")
        if not task_description:
            print("\nPlease enter a description.\n")
            continue
        else:
            break
    
    # Get the due date for the task with proper validation
    while True:
        try:
            task_due_date = input("Due date of task (DD-MM-YYYY):\t ")
            due_date_time = datetime.strptime(task_due_date, DATETIME_STRING_FORMAT)
            break
        except ValueError:
            print("Invalid datetime format. Please use the format specified")

    # Get the current date and time
    curr_date = datetime.now()

    # Create a new task dictionary
    new_task = {
        "username": task_username,
        "title": task_title,
        "description": task_description,
        "due_date": due_date_time,
        "assigned_date": curr_date,
        "completed": False
    }

    # Append the new task to the task_list
    task_list.append(new_task)
    
    # Update the tasks.txt file with the new task information
    with open("tasks.txt", "a", encoding="utf-8") as task_file:
        task_file.write(f"{new_task['username']},{new_task['title']},{new_task['description']},"
                        f"{new_task['due_date'].strftime(DATETIME_STRING_FORMAT)},"
                        f"{new_task['assigned_date'].strftime(DATETIME_STRING_FORMAT)},"
                        f"{'Yes' if new_task['completed'] else 'No'}\n")

    print("\nTask successfully added.")
    print("_" * 80)


def view_all():
    """
    Display all tasks from the 'tasks.txt' file.

    This function reads tasks from the 'tasks.txt' file, displays each task's formatted information,
    including task number, title, assigned user, dates, and description.

    If there are no tasks, it prints a message indicating that there are no tasks.

    The function utilizes the read_task_file() function to retrieve the task list.

    Note: This function assumes that tasks are stored in the 'tasks.txt' file in a specific format.

    Output:
    - Prints the formatted information of all tasks stored in 'tasks.txt'.
    """
    print("_" * 80)
    print("\n\t\t\033[4mVIEW ALL TASKS\033[0m")
    print()

    # Read tasks from the 'tasks.txt' file
    task_list = read_task_file()

    if not task_list:
        print("\nThere are no tasks.")

    else:
        # Display information for each task
        for idx, t in enumerate(task_list, start=1):
            # Display formatted task information with task number
            disp_str = f"\nTask {idx}:\t\t\t {t['title']}\n"
            disp_str += f"Assigned to: \t\t {t['username']}\n"
            disp_str += f"Date Assigned: \t\t {t['assigned_date'].strftime('%d-%m-%Y')}\n"
            disp_str += f"Due Date: \t\t {t['due_date'].strftime('%d-%m-%Y')}\n"
            disp_str += f"Task Description: \t {t['description']}"
            print(disp_str)
            print("_ " * 40)
            
        print("_" * 80)


def update_task_file(tasks):
    """
    Update the 'tasks.txt' file with the provided list of tasks.
    This function takes a list of tasks, where each task is represented as a dictionary, and updates
    the 'tasks.txt' file with the task details. It converts the list of tasks into a formatted string
    and writes it to the file. If tasks is a string, it is converted to a list of dictionaries.
    """

    # If tasks is a string, convert it to a list of dictionaries
    if isinstance(tasks, str):
        tasks = [dict(zip(['username', 'title', 'description', 'due_date', 'assigned_date', 'completed'], task.split(',')))
                 for task in tasks.strip().split('\n')]

    with open("tasks.txt", "w", encoding="utf-8") as file:
        for task in tasks:
            # Convert completed status to "Yes" or "No"
            completed_status = "Yes" if task.get('completed', False) else "No"
            
            # Write formatted task details to the file
            file.write(f"{task['username']},{task['title']},{task['description']},"
                       f"{task['assigned_date'].strftime('%d-%m-%Y')},{task['due_date'].strftime('%d-%m-%Y')},"
                       f"{completed_status}\n")


def print_task(task_id, task: dict):
    """
    Display task details.

    Parameters:
    - task_id (int): The unique identifier for the task.
    - task (dict): Dictionary containing task details.

    Output:
    - Prints formatted task details.
    """
    disp_str = f"Task: \t\t\t {task['title']}\n"
    disp_str += f"Assigned to: \t\t {task['username']}\n"            
    disp_str += f"Date Assigned: \t\t {task['assigned_date'].strftime('%d-%m-%Y')}\n"
    disp_str += f"Due Date: \t\t {task['due_date'].strftime('%d-%m-%Y')}\n"
    disp_str += f"Task Description: \t {task['description']}\n"
    disp_str += f"Completed: \t\t {'No' if not task['completed'] else 'Yes'}\n"
    print(f"\nTask No: {task_id}\n" + disp_str)
    print("_ " * 40)


def view_mine(curr_user, task_list):
    """
    Display tasks assigned to the current user.

    This function takes the current user's username and the list of tasks, filters the tasks assigned to the user,
    and displays formatted information about each task. It allows the user to select a task to view details, mark as
    complete, or edit. The function interacts with other functions like `mark_as_complete` and `edit_task` to perform
    these actions.
    """
    
    print("_" * 80)
    print("\n\t\t\033[4mVIEW MY TASKS\033[0m")
    print()

    # Filter tasks assigned to the current user
    tasks_assigned_to_user = [t for t in task_list if t['username'] == curr_user]

    if not tasks_assigned_to_user:
        print("You have no tasks assigned.")
    else:
        for idx, t in enumerate(tasks_assigned_to_user, start=1):
            # Display formatted task information for the current user
            disp_str = f"Task {idx}: \t\t {t['title']}\n"
            disp_str += f"Assigned to: \t\t {t['username']}\n"
            disp_str += f"Date Assigned: \t\t {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            disp_str += f"Due Date: \t\t {t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            disp_str += f"Task Description: \t {t['description']}\n"
            print(disp_str)
            print("_ " * 40 + "\n")

        # Allow the user to select a task or return to the main menu
        while True:
            selection = input("Enter the task number to view details or enter '-1' to return to the main menu: ")

            if selection == '-1':
                return None
            
            try:
                task_index = int(selection) - 1
                if 0 <= task_index < len(tasks_assigned_to_user):
                    # Valid task index for the current user
                    selected_task = tasks_assigned_to_user[task_index]
                    print("\n\033[4mSelected Task Details\033[0m\n")
                    print(f"Title: \t\t\t {selected_task['title']}")
                    print(f"Assigned to: \t\t {selected_task['username']}")
                    print(f"Date Assigned: \t\t {selected_task['assigned_date'].strftime(DATETIME_STRING_FORMAT)}")
                    print(f"Due Date: \t\t {selected_task['due_date'].strftime(DATETIME_STRING_FORMAT)}")
                    print(f"Task Description: \t {selected_task['description']}\n")
                    print(f"Status: \t\t {'Completed' if selected_task['completed'] else 'Not Completed'}\n")
                    print("_ " * 40 + "\n")
                     
                    task_options = input("Enter 'c' to mark as complete, 'e' to edit, or '-1' to return to the main menu: ").lower()

                    while task_options not in ['c', 'e', '-1']:
                        task_options = input("Please enter 'c' to mark as complete, 'e' to edit, or '-1' to return to menu: ").lower()

                    if task_options == 'c':
                        selected_task['completed'] = True
                        update_task_file(task_list)
                        print("\nTask marked as complete\n")
                                       
                    elif task_options == 'e':
                        edit_task(selected_task, task_list)
                        
                    elif task_options == '-1':
                        break  # Return to the main menu
    
                    else:
                        print("Invalid task number. Please enter a valid task number.")
            
                else:
                    print("\nInvalid task number. Please enter a valid task number.\n")

            except ValueError:
                print("\nInvalid input. Please try again.\n")


def edit_task(selected_task, task_list):
    """
    Edit the details of a task.

    This function allows the user to input new details for a task,
    including title, description, and due date. It then updates the task attributes
    and resets the completed status before updating the 'tasks.txt' file with the modified task list.
    """
    # Check if the task is completed before allowing edits
    if selected_task['completed']:
        print("\nCannot edit a completed task.\n")
        return

    print("\n\033[4mEdit Task\033[0m")

    while True:
        new_username = input("Enter the new user:\t\t ").lower()
        # Check if the new_username exists in the user file
        if new_username in username_password:
            break
        else:
            print("\nUser not found. Please enter a valid username.\n")

    while True:
        try:
            new_due_date = input("New Due Date (DD-MM-YYYY):\t ")
            due_date_time = datetime.strptime(new_due_date, "%d-%m-%Y")
            break  # Break the loop if the input is a valid date
        except ValueError:
            print("Invalid date format. Please enter the date in the format DD-MM-YYYY.")


    new_task = input("New Title:\t\t\t ")
    new_description = input("New Description:\t\t ")
    

    try:
        due_date_time = datetime.strptime(new_due_date, "%d-%m-%Y")
        # Update task attributes with new values
        selected_task['username'] = new_username
        selected_task['due_date'] = due_date_time
        selected_task['title'] = new_task
        selected_task['description'] = new_description
        selected_task['completed'] = False  # Reset completed status
        update_task_file(task_list)
        print("\nTask has been edited successfully.\n")
        print("_" * 80 + "\n")
    except ValueError:
        print("Invalid datetime format. Task not edited.")


def load_tasks_from_file():
    """
    Load tasks from the 'tasks.txt' file and return a list of dictionaries representing tasks.

    This function reads the contents of the 'tasks.txt' file, converts each line into a dictionary,
    and compiles a list of tasks. Each dictionary represents a task with attributes like username, title,
    description, due date, assigned date, and completion status.
    """
    try:
        with open("tasks.txt", "r", encoding="utf-8") as file:
            lines = file.readlines()

        # Convert lines to a list of dictionaries
        tasks = [dict(zip(['username', 'title', 'description', 'due_date', 'assigned_date', 'completed'], line.strip().split(',')))
                 for line in lines]

        return tasks

    except FileNotFoundError:
        print("File not found. Returning an empty list.")
        return []


def generate_task_overview(task_list):
    """
    TGenerate a summary of task completion status and write it to a text file.

    This function takes a list of tasks and calculates the total number of tasks,
    completed tasks, incomplete tasks, overdue tasks, and the corresponding percentages.
    It then writes this information to a text file named 'task_overview.txt'.
    """

    # Set variables to 0
    completed_tasks = 0
    uncompleted_tasks = 0
    overdue_tasks = 0

    # For each task, update variables accordingly
    for task in task_list:
        completed_status = task.get("completed", False)
        if completed_status:
            completed_tasks += 1
        elif "due_date" in task:
            due_date = task["due_date"]
            if isinstance(due_date, str):
                due_date = datetime.strptime(due_date, "%d-%m-%Y")

            if datetime.today() > due_date:
                uncompleted_tasks += 1
                overdue_tasks += 1
            else:
                uncompleted_tasks += 1
        else:
            uncompleted_tasks += 1

    total_tasks = len(task_list)

    # Calculate percentages for each variable
    try:
        pc_complete = (completed_tasks / total_tasks) * 100
        pc_incomplete = (uncompleted_tasks / total_tasks) * 100
        pc_overdue = (overdue_tasks / total_tasks) * 100

    # If there are no tasks at all, set all percentages to 0
    except ZeroDivisionError:
        pc_complete = pc_incomplete = pc_overdue = 0

    with open("task_overview.txt", "w", encoding="utf-8") as report_file:
        report_file.write("\tTask Overview Report\n\n")
        report_file.write(f"Total Tasks: \t\t\t {total_tasks}\n")
        report_file.write(f"Completed Tasks: \t\t {completed_tasks}\n")
        report_file.write(f"Incomplete Tasks: \t\t {uncompleted_tasks}\n")
        report_file.write(f"Overdue Tasks: \t\t\t {overdue_tasks}\n")
        report_file.write(f"Percentage of completed Tasks: \t {pc_complete:.0f}%\n")
        report_file.write(f"Percentage of Incomplete Tasks:  {pc_incomplete:.0f}%\n")
        report_file.write(f"Percentage of Overdue Tasks: \t {pc_overdue:.0f}%\n")


def generate_user_overview(username_password, task_list):
    """
    The function `gen_user_overview` generates a detailed overview of 
    tasks assigned to each user, including completion status and 
    overdue tasks, and writes this information to a text file.
    """
    total_users = len(username_password)
    total_tasks = len(task_list)

    with open("user_overview.txt", "w", encoding="utf-8") as report_file:
        report_file.write("----------------------------------------\n")
        report_file.write("\tUser Overview Report\n\n")
        report_file.write(f"Total number of users: \t\t {total_users}\n")
        report_file.write(f"Total number of Tasks: \t\t {total_tasks}\n")
        report_file.write("-----------------------------------------\n")

        for current_user in sorted(username_password):
            user_tasks_list = [task for task in task_list if task['username'] == current_user]

            user_total_tasks = len(user_tasks_list)

            # Set variables to 0
            completed_tasks = 0
            uncompleted_tasks = 0
            overdue_tasks = 0

            # For each task, update variables accordingly
            for user_task in user_tasks_list:
                if user_task["completed"]:
                    completed_tasks += 1
                elif datetime.today() > user_task["due_date"]:
                    uncompleted_tasks += 1
                    overdue_tasks += 1
                else:
                    uncompleted_tasks += 1
                
            # Calculate percentages for each variable
            try:
                pc_assigned = (user_total_tasks / total_tasks) * 100
                pc_completed = (completed_tasks / user_total_tasks) * 100
                pc_uncompleted = (uncompleted_tasks / user_total_tasks) * 100
                pc_overdue = (overdue_tasks / user_total_tasks) * 100

            # If user has no tasks assigned, set all percentages to 0
            except ZeroDivisionError:
                pc_assigned = pc_completed = pc_uncompleted = pc_overdue = 0

            report_file.write(f"\nUser: \t\t\t\t {current_user}\n")
            report_file.write(f"Total Tasks Assigned: \t\t {user_total_tasks}\n")
            report_file.write(f"Percentage of Total Tasks: \t {pc_assigned:.0f}%\n")
            report_file.write(f"Percentage of Completed Tasks: \t {pc_completed:.0f}%\n")
            report_file.write(f"Percentage of Incomplete Tasks:  {pc_uncompleted:.0f}%\n")
            report_file.write(f"Percentage of Overdue Tasks: \t {pc_overdue:.0f}%\n")


def login(username_password):
    """Handle the user login process.

    This function prompts the user for their username and password, checks the entered
    credentials against the provided `username_password` dictionary, and returns the
    username if the login is successful. If the username is not found or the password
    is incorrect, the function continues to prompt the user until valid credentials
    are provided.
    """

    while True:
        print("_" * 80 + "\n")
        print("\033[4mLOGIN\033[0m")
        curr_user = input("\033[1mUsername:\033[0m ").lower()

        # Check if the entered username exist
        if curr_user not in username_password.keys():
            print("Sorry, I couldn't find an account with that username.")
            continue

        curr_pass = input("\033[1mPassword:\033[0m ")

        if username_password[curr_user] != curr_pass:
            print("Incorrect password. Please try again.")
            continue

        else:
            print("\nLogin Successful!")
            return curr_user
        
# Load tasks from file
task_list = load_tasks_from_file()

#====Login Section====

# Check if the user.txt file exists, if not, create it with a default admin account
if not os.path.exists("user.txt"):
    with open("user.txt", "w", encoding="utf-8") as default_file:
        default_file.write("admin;password")

# Read in user_data from the user.txt file
with open("user.txt", 'r', encoding="utf-8") as user_file:
    user_data = user_file.read().split("\n")

# Convert user_data to a dictionary
username_password = {}
for user in user_data:
    # Check if user is not an empty string
    if user:
        # Split only if the string is not empty
        username, password = user.split(';')
        username_password[username] = password

#Perform user login
curr_user = login(username_password)
print("_" * 80)

while True:
    print("\n\t\t\033[4mMAIN MENU\033[0m")
    print()
    #Display menu options
    menu = input('''Select one of the following Options below:
                 
    r  - \tRegister a user
    a  - \tAdd a task
    va - \tView all tasks
    vm - \tView my tasks
    gr - \tGenerate reports
    ds - \tDisplay statistics
    e  - \tExit
    : ''').lower()
    print()

    if menu == 'r':
        # Register a new user
        reg_user()

    elif menu == 'a':
        # Add a new task
        add_task()

    elif menu == 'va':
        # View all tasks
        task_list = read_task_file()
        view_all()

    elif menu == 'vm':
        # View tasks assigned to the logged-in user
        task_list = read_task_file()
        view_mine(curr_user, task_list)
    
    elif menu == 'gr' and curr_user == 'admin':
        # Generate reports (admin-only)
        generate_task_overview(task_list)
        generate_user_overview(username_password, task_list)
        print("_" * 80 + "\n")
        print("\nReports generated successfully.\n")
        print("_" * 80 + "\n")

    elif menu == 'ds' and curr_user == 'admin':
        # Display statistics (admin-only) or generate reports if not exist
        print("_" * 80 + "\n")
        print("\n\t\t\033[4mSTATISTICS\033[0m\n")
        
        if not os.path.exists("task_overview.txt") or not os.path.exists("user_overview.txt"):
            # Generate reports if not exist         
            generate_task_overview(task_list)
            generate_user_overview(username_password, task_list)
            print("Reports generated successfully.")
            
        # Read and display statistics from the existing reports
        with open("task_overview.txt", "r", encoding="utf-8") as task_report_file:
            task_report_data = task_report_file.read()
            print(task_report_data)

        with open("user_overview.txt", "r", encoding="utf-8") as user_report_file:
            user_report_data = user_report_file.read()
            print(user_report_data)

        print("Reports displayed successfully.")        
        print("_" * 80 + "\n")   
      
    elif menu == 'e':
        # Exit the program
        print('Goodbye!')
        break

    else:
        # Invalid input, prompt the user to try again
        print("Invalid input, Please Try again.")