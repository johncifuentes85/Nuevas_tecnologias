from classes.Person import Person
#esta es una subclase de la clase person
class Employee (Person): 
    __startdate = "" #se crea la variable 
    def __init__(self, id, name, phone, state, startdate): #se llaman todas la variables incluso la clase person
        Person.__init__(self, id, name, phone, state)
        self.__startdate = startdate

    #se crean los metodos get y post
    def getStartdate (self):
        return self.__startdate
        
    def setStartdate (self, startdate):
        self.__startdate = startdate

