#To-do list app by Virginia Herrero
import datetime
from datetime import date

#Define Task class
class Task:
    """
    A class used to represent a Task
    ...

    Attributes
    ----------
    name : str
        the name of the task
    due_date : date
        the due date of the task
    completed : boolean
        completed status of the task set by default as False

    Methods
    -------
    change_name(new_name)
        changes the name of the task for a new one
    change_due_date(new_date)
        changes the due date of the task for a new one
    change_status()
        changes the completed status to completed (True)
    """

    #Define instance attributes
    def __init__(self, name, due_date):
        """
        Parameters
        ----------
        name : str
            the name of the task
        due_date : date
            the due date of the task
        completed : boolean
            completed status of the task set by default as False
        """
        self.name = name
        self.due_date = due_date
        self.completed = False #Set status as completed as False
        
    #Define methods    
    def change_name(self, new_name):
        """
        Changes the name of the task for a new one
        
        Parameters
        ----------
        new_name : str
            new name for the task
        """
        self.name = new_name

    def change_due_date(self, new_date):
        """
        Changes the due date of the task for a new one

        Parameters
        ----------
        new_date : date
            new due date for the task
        """
        self.due_date = new_date

    def change_status(self):
        """
        Changes the status of the task as completed
        """
        self.completed = True


#Define ToDoList class
class ToDoList:
    """
    A class used to represent a To Do List
    ...

    Attributes
    ----------
    tasks : list
        a list of type Task objects

    Methods
    -------
    add task(new_task)
        adds a new element of type Task to the list of tasks
    edit task(task_name_to_edit)
        edits attributes of the Task object in the list of tasks
    complete_task(task_name_to_complete)
        changes the status of the Task object to completed (True)
    delete_task(task_name_to_delete)
        deletes the Task object from the list of tasks
    show_all_tasks()
        shows all elements of type Task in the list of tasks
    show_completed_task()
        shows all elements of type Task that have the attribute completed set as True in the list of tasks
    show_todays_tasks()
        show all elements of type Taskt that have the attribute due_date set as today in the list of tasks
    """
    #Define class instance attributes
    def __init__(self):
        """
        Parameters
        ----------
        tasks: list
            a list of type Task objects
        """
        self.tasks = []
    
    #Define class methods which are the app functions
    def add_task(self, new_task):
        """
        Adds a new element of type Task to the list of tasks

        Parameters
        ----------
        new_task : Task
            new element to add to the list of tasks
        """
        self.tasks.append(new_task)
        print(f"The task {new_task.name} was added to the to-do list!")

    def edit_task(self, task_name_to_edit):
        """
        Edits attributes of the Task object in the list of tasks

        If the string parameter is equal to the "name" attribute of the Task type object, 
        it edits the attributes of the Task object according to the option chosen by the user

        Parameters
        ----------
        task_name_to_edit : str
            name of the task (type Task) to edit
        """
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

    def complete_task(self, task_name_to_complete):
        """
        Changes the status of the Task object to completed (True)

        If the string parameter is equal to the "name" attribute of the Task type object, 
        it changes the attribute "completed" o the Task type object as True

        Parameters
        ----------
        task_name_to_complete : str
            name of the task (type Task) to mark as completed
        """
        for i in self.tasks:
            if i.name == task_name_to_complete:
                i.change_status()
                print(f"Task {i.name} was marked as completed \n")
            else:
                print(f"The task {i.name} was not found \n")
       
    def delete_task(self, task_name_to_delete):
        """
        Deletes the Task object in the list of tasks

        If the string parameter is equal to the "name" attribute of the Task type object, 
        it deletes the Task type object from the list of tasks

        Parameters
        ----------
        task_name_to_complete : str
            name of the task (type Task) to mark as completed
        """
        for i in self.tasks:
            if i.name == task_name_to_delete:
                self.tasks.remove(i)
                print(f"Task {i.name} was deleted \n")
            else:
                print(f"The task {i.name} was not found \n")
    
    def show_all_task(self):
        """
        Shows all elements in the list of tasks
        """
        if self.tasks:
            print("These are all tasks in your to-do list: ")
            for index, task in enumerate(self.tasks, start = 1):
                print(f"{index}. {task.name}, due to {task.due_date} \n")
        else:
            print("Your to-do list is empty \n")

    def show_completed_tasks(self):
        """
        Shows all elements of type Task that have the attribute "completed" set as True in the list of tasks
        """
        if self.tasks:
            print("Completed tasks on your to-do list: ")
            for index, task in enumerate(self.tasks, start = 1):
                if task.completed == True:
                    print(f"{index}. {task.name} \n")
        else:
            print("No completed tasks were found in your to-do list \n")

    def show_todays_tasks(self):
        """
        Shows all elements of type Task that have the attribute "due_date" set as today in the list of tasks
        """
        if self.tasks:
            print("Today's pending tasks: ")
            for index, task in enumerate(self.tasks, start = 1):
                if task.due_date == date.today():
                        print(f"{index}. {task.name} \n")


def display_menu():
    """
    Displays the app menu
    """
    menu = {
        1: "Add New Task",
        2: "Edit Task",
        3: "Mark Task as Completed",
        4: "Delete Task",
        5: "Show All Tasks",
        6: "Show Completed Tasks",
        7: "Show Today's Tasks",
        8: "Quit To-do List"
    }
    print("---------------")
    print("To-Do List Menu")
    print("---------------")
    for key, value in menu.items():
        print(f'{key} - {value}')
    print("---------------")

def main():
    """
    Main app loop
    
    """
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

            new_task = Task(name, due_date)
            my_todo_list.add_task(new_task)

        elif choice == "2": #Edit task
            task_name_to_edit = input("Enter the name of the task to edit: ").lower()
            my_todo_list.edit_task(task_name_to_edit)

        elif choice == "3": #Mark task as completed
            task_name_to_complete = input("Enter the name of the task to mark as completed: ").lower()
            my_todo_list.complete_task(task_name_to_complete)

        elif choice == "4": #Delete task
            task_name_to_delete = input("Enter the name of the task to delete: ").lower()
            my_todo_list.delete_task(task_name_to_delete)

        elif choice == "5": #Show all task
            my_todo_list.show_all_task()

        elif choice == "6": #Show completed tasks
            my_todo_list.show_completed_tasks()

        elif choice == "7": #Show todays tasks
            my_todo_list.show_todays_tasks()

        elif choice == "8": #Quit the app
            print("Your to-do list was closed!")
            break
        
        else:
            print("Invalid input")
        
        input("Press enter to go back to menu: ")
        display_menu()

if __name__ == "__main__":
    main()
