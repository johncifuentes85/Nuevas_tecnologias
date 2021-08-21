from classes.Teacher import Teacher #se llama la clase 

#instaciar un profesor (teacher)

Teacher1 = Teacher("14", "Juana Perez", "24512525", True, "2010-02-02", 45)
print(Teacher1.getName()) #imprime nombre
Teacher1.Contract()
Teacher1.setName("Gonzalo Gonzalez")#se cambia el nombre
print(Teacher1.getName())

