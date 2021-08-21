from Misfunciones.funciones import sumar, mensaje, calsalary, emenablee  #importo la funcion desde el archivo funciones se puede importar varias funciones
print(sumar(2,3))   
mensaje()

msalary = calsalary(300,10000)
if msalary >  0:
    print(msalary)
else:
    print("Valores invalidos para calcular el salario")


#operador terniario (primero el lado verdadedo despues hago el si con la pregunta y el rersto del codigo)
messagessalary = msalary if msalary > 0 else "Valores invalidos para calcular el salario"
print(messagessalary)

#hacerlo directamente en el print
print(msalary if msalary > 0 else "Valores invalidos para calcular el salario")

if not emenablee (0): #pregunto por el True si pregunto por el False seria (not emenablee)
    print("El empleado esta inactivo")