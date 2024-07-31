#To-do list app by Virginia Herrero

#Define task class
class Task:
    #Define instance attributes
    def __init__(self, name, due_date):
        self.name = name
        self.due_date = due_date
        self.completed = False #Set status as completed as False
        
    #Define methods    
    def change_name(self, new_name):
        self.name = new_name

    def change_due_date(self, new_date):
        self.due_date = new_date

    def change_status(self):
        self.completed = True

#Initialize the tasks list
tasks = []

#Implement app functions
#Add a new task
def add_task():
    name = input("Enter task name: ")
    due_date = input("Enter due date (dd/mm/yyyy): ")
    due_date = datetime.strptime(due_date, "%d/%m/%Y")
    new_task = Task(name, due_date)
    tasks.append(new_task)
    print(f"The task {new_task.name} was added to the to-do list!")

#Edit task
def edit_task():
    task_to_edit = input("Enter the name of the tast to edit: ")
    for task in tasks:
        if task.name == task_to_edit:
            print("Editing options: 1.Change name, 2.Change due date")
            edit = int(input("Choose an option: "))
            if edit == 1:
                edited_name = input("Enter new name: ")
                task.change_name(edited_name)
                print(f"Task name was changed to {task.edited_name}")
                
            elif edit == 2:
                edited_date = input("Enter new due date: ")
                task.change_due_date(edited_date)
                print(f"Due date was changed to {task.due_date} for the task {task.name}")
                
            else:
                print("Please, enter a correct option")
        else:
            print(f"The task {task.name} was not found")

#Mark task as completed
def complete_task():
    completed_task = input("Enter the name of the completed task: ")
    for task in tasks:
        if task.name == completed_task:
            task.change_status()
            print(f"Task {task.name} was marked as completed")
        else:
            print(f"The task {task.name} was not found")
    
#Delete task
def delete_task():
    task_to_delete = input("Enter the name of the task to delete: ")
    for task in tasks:
        if task.name == task_to_delete:
            tasks.remove(task)
            print(f"Task {task.name} was deleted")
        else:
            print(f"The task {task.name} was not found")