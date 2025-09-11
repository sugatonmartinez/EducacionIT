# Ejercicio 1
# 1- Crea Series a partir de listas y arrays
import pandas as pd
import numpy as np 

lst = [1,2,3,4,5]
lst2 = ['Agustin','Tomas','Manuel','Maria','Javier']
arr = np.array([1,2,3,4,5])
arr2 = np.array(['Agustin','Tomas','Manuel','Maria','Javier'])
arr3 = np.random.randint(1,100,12)
c = arr3.reshape(3,4)

s1 = pd.Series(lst)
print(s1)
s2 = pd.Series(lst2)
print(s2)
s3 = pd.Series(arr)
print(s3)
s4=pd.Series(arr2)
print(s4)
s5=pd.Series(arr3)
print(s5)
print(c)
s6=pd.Series(c[:,0])
print(s6)
print('-'*50)
#2- Crea dataframes a partir de listas anidadas y de arrays anidados
anid = [[1,2],[3,4],[5,6]]
anid2 = [['Agustin','Tomas'],['Manuel','Maria'],['Javier','Ana']]
arrandi = [[1,2,3],
           [4,5,6],
           [7,8,9]]
arrandi2 = [['Agustin','Tomas'],
            ['Manuel','Maria'],
            ['Javier','Ana']]

df1 = pd.DataFrame(anid)
print(df1)
df2= pd.DataFrame(anid2)
print(df2)
df3 = pd.DataFrame(arrandi)
print(df3)
df4 = pd.DataFrame(arrandi2)
print(df4)
df5 = pd.DataFrame(c)
print(df5)

#3- Crear dataframes especificando etiquetas para las columnas 
df2.columns = ['A','B']
print(df2)
df5.columns = ['A','B','C','D']
print(df5)

#4- Cargar el dataframe del titanic y visualizar la información del mismo 
ruta = "C:\\Users\\sugat\\OneDrive\\Escritorio\\Data sience\\Analyst\\Py_DA\\titanic.csv" # La dirección depende de la ruta del individuo
df_t = pd.read_csv(ruta)
print(df_t)

# Ejerccio 2
# 1- Seleccionar las columans “Survived”, “Pclass”, “Age” y “Sex”.
print(df_t[['Survived','Pclass','Age','Sex']].head())

# 2- Seleccionar las filas 200 a 400 de las columnas 'Name' y 'Age'
print(df_t[['Name','Age']].iloc[200:401])

# 3- Cambiar el nombre de la columna 'Passengerid' a 'ID'
data = df_t.copy()
data.rename(columns={'PassengerId': 'ID'},inplace=True)
print(data)

#4- Seleccionar los datos de las muejres de primera clase
mascara = data[(data['Sex']=='female')&(data['Pclass']==1)]
print(mascara)

#5-Seleccionar los datos de los varones menores de edad perteneciente a segunda clase 
mascara2 = data[(data['Sex']=='male')&(data['Pclass']==2)]
print(mascara2)
print('-'*150)

#Ejercicio 3
#1- Encontrar el promedio de edad de hombres y mujeres
print(data)
print(data.loc[data['Sex']=='female','Age'].mean())
print(data.loc[data['Sex']=='male','Age'].mean())
print(data.loc[data['Sex']=='female','Age'].mean(),data.loc[data['Sex']=='male','Age'].mean()) # se pueden mostrar uno al lado del otro

#2- Encontrar la cantidad de sobrevivientes de hombres y mujeres 
print(data)
surv_m= data[(data['Sex']=='male')&(data['Survived']==1)]
surv_f  = data[(data['Sex']=='female')&(data['Survived']==1)]
cant = surv_m['Survived'].count()
cant2 =  surv_f['Survived'].count()
print(surv_m)
print(f'Sobrevivieorn {cant} hombres y {cant2} mujeres')
