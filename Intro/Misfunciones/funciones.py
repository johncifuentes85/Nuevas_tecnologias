"""Definir funciones"""
def mensaje(): #definimos la funcion mensaje
    print("Hola desde la funcion mensaje")

def sumar(a,b):
    return a+b

def calsalary (nht,vh):
    salary = 0
    if nht >= 240:
        salary = nht * vh
    return salary

def emenablee (nht):
    active = True
    if nht == 0:
        active =False
    return active