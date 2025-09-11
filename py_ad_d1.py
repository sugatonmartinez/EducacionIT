#Ejercicio 1: Dada una lista de números encontrar el promedio

lst = [10,23,45,76,12]
prom = sum(lst)/len(lst)
print(f'El promedio de la lista es: {prom}')
#Ejercicio 2: Crear una lista con los primeros 10 multiplos de 5
mult_5 = [i*5 for i in range(1,11)]
print(f'Los primeros 10 multiplos de 5 son: {mult_5}')

#Ejercicio 3: Dada dos listas, crar otra que tenga los elementos que 
#estan en la primera pero no en la segunda
lst1 = [1,2,3,4,5,6,7,8]
lst2 = [5,6,7,8,9,10]
lst3 = [i for i in lst1 if i not in lst2]
print(f'Los elementos que estan en la primera lista pero no en la segunda son: {lst3}')








