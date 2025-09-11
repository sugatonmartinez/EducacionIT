import numpy as np
# Ejercicio 1 
'''
A- Contruir arrays a partir de una lista simple y una lista anidada usando tipos numéricos distintos para cada una
B- Contruir un array lineal de 36 elementos cambiar el shape para que tenga:
3 filas y 12 columnas
4 columnas
'''

lst = [12,30.5,50,4,22.1]

matriz = [[7,8.23,12],[18,20,11.11]]

a = np.array(lst)
print(a)
print('-'*50)
b = np.array(matriz)
print(b)
print('-'*50)
c =  np.random.randint(1,100,36)
print(c)
print('-'*50)
d = c.reshape(3,12)
print(d)
print('-'*50)
e = c.reshape(9,4)
print(e)
print('-'*50)
#Ejercicio 2
'''
Dado un vector de pesos(kg) y otro de altura(metros)
Calcular el índice de masa corporal(vector imc)
'''
pesos = np.array([50,65.5,89.2,100])
alturas = np.array([1.6,1.7,1.8,1.75])
imc = pesos / (alturas**2)
print(imc)
print('-'*50)
#Ejercicio 3
'''
A- Crear un vector de 10 elementos todos 0
B- Crear vector de 10 numeros al azar
C- Crear una matriz  2x3 y multiplicarla por su traspuesta
A*AT
'''
#A
vect = np.zeros(10)
print(vect)
print('-'*50)
#B
vect2 = np.random.randint(0,101,10)
print(vect2)
print('-'*50)
#C
vect3 = np.array([[11,23,7],
                  [37,88,40]])
print(vect3)
print('-'*50)
print(vect3.T)
print('-'*50)
print(vect3@vect3.T)


