import pandas as pd
import numpy as np
import ast
import json
from collections import Counter


rows = []
with open('steam_games.json', 'r') as f:
    for line in f.readlines():
        rows.append(ast.literal_eval(line))

df = pd.DataFrame(rows)


#Genres por año
def GPA(year: str):
    df.dropna(subset='genres', inplace= True)
    ventas = df.loc[df["release_date"].str.contains(year) == True]
    lista0 = ventas['genres'].tolist()
    B=[]
    for lista1 in lista0:
        for numero in lista1:
            B.append(numero)

    a = dict(Counter(B))
    sorteddict=sorted(a)
    sorteddict=sorteddict[0:4]
    return sorteddict

#Juegos por año
def JPA(year: str):
    if type(year) != str:
        year = str(year)
    data =  df.loc[df["release_date"].str.contains(year) == True]
    data["app_name"].apply(lambda x: str (x))
    data["release_date"].apply(lambda x: str(x))
    data = data.dropna(subset=["app_name"])
    names_list = [i for i in data["app_name"]]
    return {year: names_list}

#Specs por año
def SPPA(year: str):
    df.dropna(subset='specs', inplace= True)
    repetidos = df.loc[df["release_date"].str.contains(year) == True]
    lista0 = repetidos['specs'].tolist()
    B=[]
    for lista1 in lista0:
        for numero in lista1:
            B.append(numero)
    
    a = dict(Counter(B))
    specs_1 = GT5(a)
    return specs_1

def GT5(diccionario):
    diccionario = dict(sorted(diccionario.items(), key=lambda x: x[1], reverse=True))
    primeros_5_valores = {}
    contador = 0
    for clave, valor in diccionario.items():
        primeros_5_valores[clave] = valor
        contador += 1
        if contador == 5:
            break
    return primeros_5_valores


#Earlyaccess por año
def EPA(year: str):
    df.dropna(subset='early_access', inplace= True)
    cantidad_juegos = df.loc[df["release_date"].str.contains(year) == True]
    lista = cantidad_juegos['early_access'].tolist()
    diccionario = {year: len(lista)}
    return diccionario

#Sentiment por año
def SPA(year: str):
    sentiments_list = ['Mixed', 'Mostly Positive', 'Very Positive', 'Overwhelmingly Positive', 'Very Negative', 'Positive', 'Mostly Negative', 'Negative', 'Overwhelmingly Negative']
    data = df.loc[df['release_date'].str.contains(year) == True]
    data_filt = data.loc[data['sentiment'].isin(sentiments_list)]
    result = []
    for i in sentiments_list:
        result.append((i, len(data_filt.loc[data_filt['sentiment'] == i])))
    result = dict(result)
    return {year: result}

#Metascore por año
def MPA(year: str):
    data = df.loc[df['release_date'].str.contains(year) == True]
    data = data.dropna(subset=['app_name'])
    data_sorted = data.sort_values(by='metascore', ascending=False)
    top_5 = data_sorted.head(5)
    result = {}
    for idx, row in top_5.iterrows():
        result[row['app_name']] = row['metascore']
    return {year: result}

# ============================================================================================= #
# Funcion del modelo de prediccion

def Futureprice(variables: str):
    string_numbers = variables.split(", ")
    integer_list = [int(number) for number in string_numbers]
    if len(integer_list) == 13:
        price_pred = loaded_model.predict(np.array(integer_list).reshape(1, -1))[0].round(2)
        RMSE = '4.68'
        return {'price prediction': str(price_pred), 'RMSE': RMSE}
    elif len(integer_list) < 13:
        return {'error': 'se insertaron variables de menos'}
    elif len(integer_list) > 13:
        return {'error': 'se insertaron variables demas'}
    
    








