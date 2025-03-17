import pandas as pd
import numpy as np
data = {
    "ID": [1,2,3,4,5],
    "Nombre": [ "Ana","Carlos",np.nan,"Pedro","Lucia"],
    "Edad": [25,np.nan,30,40,np.nan],
    "Salario": [2500,3200,4000,np.nan,5000]
    
    }
df= pd.DataFrame(data)
print(df)
print("\n valores nulos por columna")
print(df.isnull().sum())


df_sin_nulos_filas=df.dropna()
print("\n elimina Filas con valores nulos")
print(df_sin_nulos_filas)

df_sin_nulos_columnas=df.dropna(axis=1)
print("Elimina Columnas con valores nulos")
print(df_sin_nulos_columnas)


df["Edad"].fillna(df["Edad"].mean(),inplace=True)

df["Salario"].fillna(df["Salario"].median(),inplace=True)

df["Nombre"].fillna(df["Nombre"].mode()[0],inplace=True)
