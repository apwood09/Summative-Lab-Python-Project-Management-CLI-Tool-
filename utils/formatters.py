from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console()

def print_welcome():
    """displays a stylish welcome header."""
    console.print(Panel.fit(
        "🚀 [bold cyan]Project Management CLI v1.0[/bold cyan]\n"
        "[italic]Admin tool for Users, Projects, and Tasks[/italic]",
        border_style="bright_blue"
    ))

def format_user_table(users):
    """
    renders a list of User objects into a Rich Table.
    """
    table = Table(show_header=True, header_style="bold magenta", title="[bold]Registered Users[/bold]")
    table.add_column("ID", style="dim", width=6)
    table.add_column("Full Name", min_width=20)
    table.add_column("Email Address", min_width=30)

    if not users:
        console.print("[yellow]No users found in system.[/yellow]")
        return

    for user in users:
        table.add_row(str(user.id), user.name, user.email)
    
    console.print(table)

def format_project_list(projects, owner_name):
    """
    renders a list of Project objects for a specific user.
    """
    table = Table(title=f"Projects assigned to [bold cyan]{owner_name}[/bold cyan]")
    table.add_column("ID", justify="right", style="cyan", no_wrap=True)
    table.add_column("Title", style="white")
    table.add_column("Due Date", style="green")
    table.add_column("Description", style="dim")

    for proj in projects:
        table.add_row(str(proj.id), proj.title, proj.due_date, proj.description)
    
    console.print(table)

def format_task_table(tasks, project_title):
    """
    renders a list of Task objects. Color-codes status for clarity.
    """
    table = Table(title=f"Tasks for [bold yellow]{project_title}[/bold yellow]")
    table.add_column("ID", style="dim")
    table.add_column("Task Name")
    table.add_column("Assigned To", style="blue")
    table.add_column("Status", justify="center")

    for task in tasks:
        # dynamic color coding based on task status
        color = "green" if task.status == "Completed" else "yellow"
        if task.status == "Blocked": color = "red"
        
        status_display = f"[{color}]{task.status}[/{color}]"
        table.add_row(str(task.id), task.title, task.assigned_to, status_display)
    
    console.print(table)

def print_error(message):
    """error output."""
    console.print(f"[bold red]ERROR:[/bold red] {message}")

def print_success(message):
    """success output."""
    console.print(f"[bold green]SUCCESS:[/bold green] {message}")