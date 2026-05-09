🚀 Project Management CLI Tool

A command-line interface for managing users, projects, and tasks. Built with Python, featuring strict data validation, JSON persistence, and a full Pytest suite.

🛠 Features
User Management: create & track project owners

Project Tracking: manage project descriptions & due dates with (strict YYYY-MM-DD validation)

Task Workflow: assign tasks to projects & track completion status

Data Persistence: data is saved to & loaded from JSON files in the data/ directory.

Robust Error Handling: custom validation prevents invalid data from entering the system.

🚀 Getting Started
1. Installation
Ensure you have Python 3.10+ installed. fork/clone the repository and install dependencies: pip install -r requirements.txt

2. Running the Tool
Use the main.py script with various commands

Add a User:
python main.py add-user --name "Alex" --email "alex@example.com"

Add a Project:
python main.py add-project --user "Alex" --title "Website Redesign" --due "2026-12-31"

Add and Complete Tasks:
python main.py add-task --project "Website Redesign" --title "Fix Header"
python main.py complete-task --id 1

3. Running Tests
PYTHONPATH=. pytest

🧪 Logic Highlights
Encapsulation: @property and @setter decorators to protect data integrity

Path Awareness: storage utility automatically handles both relative and absolute paths, making it compatible with testing environments.

ID Auto-increment: automatically manages unique IDs for all entities without requiring manual input