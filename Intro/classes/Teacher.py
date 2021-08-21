from classes.Employee import Employee

class Teacher (Employee):
    __numberhour = 0

    def __init__(self, id, name, phone, state, startdate, numberhour ):
        Employee.__init__(self, id, name, phone, state, startdate)
        self.__numberhour = numberhour

    def getNumberhour (self):
        return self.__numberhour
    
    def setNumberhour (self, numberhour):
        self.__numberhour = numberhour