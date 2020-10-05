import numpy as np
from scipy import stats
#Definicion de variables
lista=[]
contador=0
print("*"*30, "BIENVENIDO","*"*30)

#Pregunto cuantas datos va a registrar
cantidad=int(input("Cuantos datos quieres registrar : "))
print("*"*30)
#Aqui inicio un ciclo for para preguntarle los numeros este for se va iternado hasta que llegue al numero de datos que registro arriba
for valor in range(cantidad):
    #Aqui le pregunto los numeros 
    numero=int(input("Dime los numeros de tu muestra:"))
    #Aqui voy agregando los numero a una lista cuya lista va tener todos los datos que me de 
    lista.append(numero)
    print("*"*30)

#Declaro una variable la cual va a sumar todos los datos de la lista
suma=sum(lista)
#Aqui divido la suma de los datos entre la cantidad de datos para sacar la media
media=(suma/cantidad)

#Aqui ordeno la lista para poder sacar la moda despues 
listaordenada=sorted(lista)

#Aqui saco la mediana atravez de una funcion y le paso la lista que le quiero sacar la mediana
mediana=np.median(lista)
#Aqui le saco la moda dandole la lista de datos que ordene anteriormente
#y luego aplico una funcion mode que saca la moda
moda=stats.mode(listaordenada)

#Aqui saco la desviacion Estandar de los valores dados antes
desviacionEstandar=np.std(lista)