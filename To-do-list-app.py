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