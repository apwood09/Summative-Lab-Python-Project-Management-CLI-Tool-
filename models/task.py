from utils.storage import save_data, load_data

class Task:
    """
    represents specific task within project.
    One-to-Many Relationship: One Project -> Many Tasks.
    """
    _id_counter = 1

    # FIXED: Indented exactly 4 spaces to match _id_counter
    def __init__(self, title, project_id, assigned_to=None, status="Pending", task_id=None, **kwargs):
        """
        initializes task instance.
        """
        # 1. Handle ID logic
        self.id = task_id or kwargs.get('id') or Task._id_counter
        
        # 2. Set basic attributes
        self.title = title
        self.project_id = project_id
        self.assigned_to = assigned_to or "Unassigned"
        
        # 3. Handle Status (checking both the argument and the JSON underscore version)
        initial_status = status if status != "Pending" else kwargs.get('_status', "Pending")
        self.status = initial_status  # This triggers the @status.setter
        
        # 4. Increment counter if it's a new task
        if not task_id and 'id' not in kwargs:
            Task._id_counter += 1

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        """restricts status to specific set of allowed values."""
        allowed_statuses = ["Pending", "In Progress", "Completed", "Blocked"]
        if value not in allowed_statuses:
            # Fallback for unexpected data
            self._status = "Pending"
            return
        self._status = value

    def mark_complete(self):
        """instance method to quickly update task status to Completed."""
        self.status = "Completed"

    def __str__(self):
        """formatted string for CLI lists."""
        status_icon = "✅" if self.status == "Completed" else "⏳"
        return f"{status_icon} [{self.id}] {self.title} - Assigned to: {self.assigned_to}"

    def __repr__(self):
        return f"Task(id={self.id}, title='{self.title}', project_id={self.project_id})"

    @classmethod
    def get_by_id(cls, tasks_list, task_id):
        """class method to find a specific task object by ID."""
        for task in tasks_list:
            if task.id == int(task_id):
                return task
        return None