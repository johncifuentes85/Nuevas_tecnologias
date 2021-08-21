class Person:
    __id = "" #privado con __ de lo contrario publico
    __name = ""
    __phone = ""
    __state = True

    #constructor
    def __init__(self,id,name,phone,state):
        """self es igual que this en java se igualan las variables"""
        self.__id = id
        self.__name = name
        self.__phone = phone
        self.__state = state

    #se definen los POST y GET para recibir y enviar informacion
    def getId(self):
        return self.__id

    def setId(self, id):
        self.__id = id
    
    def getName(self):
        return self.__name

    def setName(self, name):
        self.__name = name

    def getPhone(self):
        return self.__phone

    def setPhone(self, phone):
        self.__phone = phone
    
    def getState(self):
        return self.__state

    def setState(self, state):
        self.__state = state
    
    def Contract (self):
        print("se ha definido el contrato")




