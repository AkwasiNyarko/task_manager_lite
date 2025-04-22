class Task:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.completed = False

    def mark_complete(self):
        self.completed = True

# Example usage
task_list = []

def show_menu():
    print("1. Add Task\n2. View Tasks\n3. Complete Task\n4. Exit")

# Add more logic here...
