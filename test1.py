# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 16:35:16 2023

@author: break
"""

import pandas as pd
import json

# Leer el archivo CSV
df_csv = pd.read_csv(r"D:/Krowdy/instituciones_educativas.csv")

# Leer el archivo JSON
with open(r"D:/Krowdy/Universidades.json") as f:
    json_data = json.load(f)
df_json = pd.DataFrame(json_data)

# Hacer el merge de los dataframes
df_merged = pd.merge(df_csv, df_json, left_on='value', right_on='Nombre ')

# Seleccionar las columnas que se necesitan
df_final = df_merged[['candidateId', 'value', 'Nombre ']]
df_final = df_final.rename(columns={'Nombre ': 'Universidad_Homologada'})

# Ver el resultado
print(df_final.head())

df_final.to_csv('D:/Krowdy/universidades_homologadas.csv', index=False)


# Leer el archivo json con las universidades
universidades = pd.read_json('D:/Krowdy/Universidades.json')

# Seleccionar las columnas "Nombre" y "Siglas" y renombrarlas
sinonimos = universidades[['Nombre ', 'Siglas ']].rename(columns={'Nombre ': 'nombre_universidad', 'Siglas ': 'sinonimos'})

print(sinonimos.head())
# Guardar el dataframe en un archivo json
sinonimos.to_json('D:/Krowdy/sinonimos_universidades.json', orient='records')