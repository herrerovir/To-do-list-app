#To-do list app by Virginia Herrero

from datetime import datetime

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

#Define ToDoList class
class ToDoList:
    #Define class instance attributes
    def __init__(self):
        self.tasks = []
    
    #Define class methods which are the app functions
    #Add a new task
    def add_task(self, task):
        self.tasks.append(task)
        print(f"The task {task.name} was added to the to-do list!")

    #Edit task
    def edit_task(self, task_name):
        for i in self.tasks:
            if i.name == task_name:
                print("Editing options: 1.Change name, 2.Change due date")
                edit = int(input("Choose an option: "))
                if edit == 1:
                    edited_name = input("Enter new name: ")
                    i.change_name(edited_name)
                    print(f"Task name was changed to {i.name} \n")
                    
                elif edit == 2:
                    edited_date = input("Enter new due date: ")
                    i.change_due_date(edited_date)
                    print(f"Due date was changed to {i.due_date} for the task {i.name}")
                    
                else:
                    print("Please, enter a correct option")
            else:
                print(f"The task {i.name} was not found")

    #Mark task as completed
    def complete_task(self, task_name):
        for i in self.tasks:
            if i.name == task_name:
                i.change_status()
                print(f"Task {i.name} was marked as completed")
            else:
                print(f"The task {i.name} was not found")
       
    #Delete task
    def delete_task(self, task):
        for i in self.tasks:
            if i.name == task:
                self.tasks.remove(i)
                print(f"Task {i.name} was deleted")
            else:
                print(f"The task {i.name} was not found")