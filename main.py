import argparse
from models.user import User
from models.project import Project
from models.task import Task
from utils.storage import save_data, load_data
from utils.formatters import (
    print_welcome, format_user_table, format_project_list, 
    format_task_table, print_error, print_success
)

def main():
    print_welcome()
    
    parser = argparse.ArgumentParser(description="Admin Project Management Tool")
    subparsers = parser.add_subparsers(dest="command")

    # --- USER COMMANDS ---
    user_parser = subparsers.add_parser("add-user")
    user_parser.add_argument("--name", required=True)
    user_parser.add_argument("--email", required=True)

    subparsers.add_parser("list-users")

    # --- PROJECT COMMANDS ---
    proj_parser = subparsers.add_parser("add-project")
    proj_parser.add_argument("--user", required=True, help="Name of the user owner")
    proj_parser.add_argument("--title", required=True)
    proj_parser.add_argument("--desc", default="No description")
    proj_parser.add_argument("--due", required=True, help="Format: YYYY-MM-DD")

    subparsers.add_parser("list-projects")

    # --- TASK COMMANDS ---
    task_parser = subparsers.add_parser("add-task")
    task_parser.add_argument("--project", required=True, help="Title of the project")
    task_parser.add_argument("--title", required=True)
    task_parser.add_argument("--assigned", default="Unassigned")

    task_list_parser = subparsers.add_parser("list-tasks")
    task_list_parser.add_argument("--project", required=True)

    # Complete Task Command
    complete_parser = subparsers.add_parser("complete-task")
    complete_parser.add_argument("--id", required=True, type=int)

    args = parser.parse_args()

    # --- LOGIC HANDLING ---

    if args.command == "add-user":
        users = load_data("users.json", User)
        try:
            new_user = User(args.name, args.email)
            users.append(new_user)
            save_data("users.json", users)
            print_success(f"User {args.name} created!")
        except ValueError as e:
            print_error(e)

    elif args.command == "list-users":
        users = load_data("users.json", User)
        format_user_table(users)

    elif args.command == "add-project":
        users = load_data("users.json", User)
        projects = load_data("projects.json", Project)
        
        # Find user by name to get ID
        owner = next((u for u in users if u.name.lower() == args.user.lower()), None)
        if not owner:
            print_error(f"User '{args.user}' not found. Create them first!")
            return

        # Handle potential validation errors from the Project Model
        try:
            new_proj = Project(args.title, args.desc, owner.id, args.due)
            projects.append(new_proj)
            save_data("projects.json", projects)
            print_success(f"Project '{args.title}' linked to {owner.name}.")
        except ValueError as e:
            print_error(e)

    elif args.command == "list-projects":
        projects = load_data("projects.json", Project)
        format_project_list(projects)

    elif args.command == "add-task":
        projects = load_data("projects.json", Project)
        tasks = load_data("tasks.json", Task)
        
        target_proj = Project.find_by_title(args.project, projects)
        if not target_proj:
            print_error(f"Project '{args.project}' not found.")
            return

        new_task = Task(args.title, target_proj.id, args.assigned)
        tasks.append(new_task)
        save_data("tasks.json", tasks)
        print_success(f"Task added to {target_proj.title}.")

    elif args.command == "list-tasks":
        projects = load_data("projects.json", Project)
        tasks = load_data("tasks.json", Task)
        
        target_proj = Project.find_by_title(args.project, projects)
        if target_proj:
            proj_tasks = [t for t in tasks if t.project_id == target_proj.id]
            format_task_table(proj_tasks, target_proj.title)
        else:
            print_error("Project not found.")

    elif args.command == "complete-task":
        tasks = load_data("tasks.json", Task)
        target_task = Task.get_by_id(tasks, args.id)
        
        if target_task:
            target_task.mark_complete()
            save_data("tasks.json", tasks)
            print_success(f"Task {args.id} marked as Completed! ✅")
        else:
            print_error(f"Task ID {args.id} not found.")

    else:
        if args.command:
            parser.print_help()

if __name__ == "__main__":
    main()