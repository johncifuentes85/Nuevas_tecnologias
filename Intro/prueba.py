print("Hola, mundo desde python") #imprimir 
a = 2500 
b = "Feria de Flores" 
c = False 
d = [12, 45, 67, 89, 120, 23] #lista de numeros 
''' este es un comentario de varias lineas''' 

#diccionario     
datosemp = {"cedula":"43","nombre":"peranito", "telefono":["2291100","3112564585"]} 
print("evento: ",b)#imprime la variable b hace salto de linea 
print("evento: ",b,end='') #sin salto de linea 
print(" en la ciudad de medellin") 
print("\n\n\n Texto de prueba con salto de linea \n\n") #\n son saltos de linea 
print(f"Evento que se celebra en Medellin {b}, en el mes de agosto") #f se utiliza para concatenar con una variable 

#condicional 
if a> 2300 and not c: 
    print("Tiene derecho a bono de Feria") 
    print("Visita las fondas de mi tierra") 
else: 
    print("No tiene derecho a bono de mi tierra") 

#selector multiple 
categoria = "E" 
valorcopago = 0 
if categoria == "A": 
    valorcopago = 5000 
elif categoria == "B": 
    valorcopago = 7500 
elif categoria == "C": 
    valorcopago = 10000 
elif categoria == "D": 
    valorcopago = 12500 
else: #otro caso
    valorcopago = 1200 

print(f"El valor del copago es: {valorcopago}") 

#operador ternario 
estado = "Activo" if not c else 2 
print(estado) 

#while 
i = 1 
while i < 10: 
    print(f" 3 x {i} = {i*3}") 
    i += 1 

#for 
for nro in d: #recorre lista  
    print(nro) 

for letra in "CESDE": #se le púede dar un valor a la variable 
    print(letra, end='')

for nro in range(6): #toma un rango y lo muestra en este caso hasta 6
    print(nro)

for nro in range(20,31): # toma un rango en este caso del 20 al 31
    print(nro)

#mostrar datos del diccionario datosemp
print(datosemp['cedula']) #imprime el cedula del array
print(f"Nombre: {datosemp['nombre']}") #concatena los datos del nombre 

print(datosemp)#imprime los datos del array

for key in datosemp:
    print(key,";",datosemp[key])

print("Telefono fijo: ", datosemp['telefono'][0]) #para imprimir la posision de un dato
print("Telefono movil: ", datosemp['telefono'][1])

#capturar datos por teclado
nht = float(input("ingrese el numero de horas: "))#para hacer operaciones se debe convertir el string 
print(nht*3000)

#funciones(devuelven algo)
