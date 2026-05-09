from datetime import datetime
from .task import Task
from utils.storage import load_data

class Project:
    _id_counter = 1

    def __init__(self, title, description, user_id, due_date=None, project_id=None, **kwargs):
        # 1. Handle the ID
        self.id = project_id or kwargs.get('id') or Project._id_counter
        
        # 2. Basic attributes
        self.title = title
        self.description = description
        self.user_id = user_id
        
        # 3. Trigger validation by using the public attribute name
        self.due_date = due_date or kwargs.get('_due_date', "2000-01-01")
        
        # 4. Increment counter if new
        if not project_id and 'id' not in kwargs:
            Project._id_counter += 1

    @property
    def due_date(self):
        """The getter: returns the internal underscored value."""
        return self._due_date

    @due_date.setter
    def due_date(self, value):
        """The setter: validates format before saving to the internal value."""
        try:
            datetime.strptime(value, "%Y-%m-%d")
            self._due_date = value
        except (ValueError, TypeError):
            # This is what stops "June 1st" from being saved
            raise ValueError(f"'{value}' is an invalid date. Please use YYYY-MM-DD.")

    @classmethod
    def find_by_title(cls, title, projects_list):
        for project in projects_list:
            if project.title.lower() == title.lower():
                return project
        return None

    def get_tasks(self):
        all_tasks = load_data("tasks.json", Task)
        return [task for task in all_tasks if task.project_id == self.id]