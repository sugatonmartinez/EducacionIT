# Generar una función que reciba un iterable y devuelva
# las frencuencias de aparicion de cada elemento
# ejercicio 1
lst = [1,2,3,4,5,4,3,2,1]
lst2=[1,33,242,1242,22,33,234]
lst3= 'banana'
def frecuencia(iterable):
    frec = {}
    for n in iterable :
        if n not in frec:
            frec[n]=1     
        else:
            frec[n]+=1
    return frec        
print(frecuencia(lst))  

#ejercicio 2 
#Construir una función que se llame suma_acotados.
#Esta función debe tomar un número arbitrario de
#argumentos posicionales y un keyword argument
#llamado cota que por defecto debe tener el valor
#None. Si el argumento cota es None, debe sumar
#todos los números, sino debe sumar los números 
#que se encuentren entre –cota y cota.
def suma_acotados(*args,cota=None):
    if cota == None:
        total=sum(args)
    else:
        num =[]
        for n in args:
            if -cota <= n <= cota:  
                num.append(n)
        total=sum(num)
    return total   
print(suma_acotados(1,2,3,4,5,cota=5))
 
#ejercicio 3
''' 
Supongamos que tenemos una lista de tuplas en donde 
cada una contiene el nombre de un producto y el precio 
correspondiente. Por ejemplo:
 [("Campera", 3500), ("Mochila", 2400), 
("Zapatillas", 5200), ("Jean", 1600)]
 Ordenar los productos según su precio de mayor a menor 
usando sorted, map y funciones lambda
'''
lst_tpl=[("Campera", 3500), ("Mochila", 2400), ("Zapatillas", 5200), ("Jean", 1600)]
sort=sorted (lst_tpl, key= lambda x:x[1],reverse=False)
transformados = map(lambda x: f"{x[0]}: ${x[1]}", sort)
print(sort)
print(list(transformados))
