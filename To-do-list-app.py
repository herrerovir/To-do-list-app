#To-do list app by Virginia Herrero
import datetime
from datetime import date

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
    def edit_task(self, task_name_to_edit):
        for i in self.tasks:
            if i.name == task_name_to_edit:
                print("Editing options: 1 - Change name, 2 - Change due date")
                edit = int(input("Choose an option: "))
                if edit == 1: #change name
                    edited_name = input("Enter new task name: ").lower()
                    for j in self.tasks:
                        while j.name == edited_name:
                            print(f"{edited_name} is already used. Please, choose another name")
                            edited_name = input("Enter new task name: ").lower()
                    i.change_name(edited_name)
                    print(f"Task name was changed to {i.name} \n")
                    
                elif edit == 2: #change due date
                    while True:
                        edited_date = input("Enter new due date (dd/mm/yyyy): ")
                        try:
                            edited_date = datetime.datetime.strptime(edited_date, "%d/%m/%Y").date()
                        except ValueError:
                            print("Invalid date format. Please enter date as dd/mm/yyyy")
                        else:
                            break
                    i.change_due_date(edited_date)
                    print(f"Due date was changed to {i.due_date} for the task {i.name} \n")
                    
                else:
                    print("Please, enter a correct option \n")
            else:
                print(f"The task {i.name} was not found \n")

    #Mark task as completed
    def complete_task(self, task_name_to_complete):
        for i in self.tasks:
            if i.name == task_name_to_complete:
                i.change_status()
                print(f"Task {i.name} was marked as completed \n")
            else:
                print(f"The task {i.name} was not found \n")
       
    #Delete task
    def delete_task(self, task_name_to_delete):
        for i in self.tasks:
            if i.name == task_name_to_delete:
                self.tasks.remove(i)
                print(f"Task {i.name} was deleted \n")
            else:
                print(f"The task {i.name} was not found \n")
    
    def show_all_task(self):
        if self.tasks:
            print("All tasks in your to-do list: ")
            for index, task in enumerate(self.tasks, start = 1):
                print(f"{index}. {task.name}, due to {task.due_date} \n")
        else:
            print("Your to-do list is empty \n")

    def show_completed_tasks(self):
        if self.tasks:
            print("Completed tasks on your to-do list: ")
            for index, task in enumerate(self.tasks, start = 1):
                if task.completed == True:
                    print(f"{index}. {task.name} \n")
        else:
            print("No completed tasks were found in your to-do list \n")

    def show_todays_tasks(self):
        if self.tasks:
            print("Tasks due to today: ")
            for index, task in enumerate(self.tasks, start = 1):
                if task.due_date == date.today():
                        print(f"{index}. {task.name} \n")



#Display app menu
def display_menu():
    #App Menu
    menu = {
        1: "Add New Task",
        2: "Edit Task",
        3: "Mark Task as Completed",
        4: "Delete Task"
    }
    print("---------------")
    print("To-Do List Menu")
    print("---------------")
    for key, value in menu.items():
        print(f'{key} - {value}')
    print("---------------")

#Main app loop
def main():
    my_todo_list = ToDoList()
    display_menu()
    while True:
        choice = input("What would you like to do? Please, choose an option: \n")

        if choice == "1": #Add new task: name and due date
            name = input("Enter task name: ").lower()
            for i in my_todo_list.tasks:
                while i.name == name:
                    print(f"{name} is already used. Please, choose another name")
                    name = input("Enter task name: ")

            while True:
                due_date = input("Enter due date (dd/mm/yyyy): ")
                try:
                    due_date = datetime.datetime.strptime(due_date, "%d/%m/%Y").date()
                except ValueError:
                    print("Invalid date format. Please enter date as dd/mm/yyyy")
                else:
                    break

            task = Task(name, due_date)
            my_todo_list.add_task(task)

        elif choice == "2": #Edit task
            task_name_to_edit = input("Enter task to edit: ").lower()
            my_todo_list.edit_task(task_name_to_edit)

        elif choice == "3": #Mark task as completed
            task_name_to_complete = input("Enter task to mark as completed: ").lower()
            my_todo_list.complete_task(task_name_to_complete)

        elif choice == "4": #Delete task
            task_name_to_delete = input("Enter task to delete: ").lower()
            my_todo_list.delete_task(task_name_to_delete)

        else:
            break
        
        input("Press enter to go back to menu: ")
        display_menu()

if __name__ == "__main__":
    main()
