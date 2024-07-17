from django.views.generic import TemplateView
from django.shortcuts import render
from django.http import JsonResponse
import random

import time
import random

import pandas as pd
import numpy as np



def crear_df_y_calcular_distancias():
    # Crear un DataFrame con 1000 elementos y 3 coordenadas (x, y, z)
    df = pd.DataFrame(np.random.rand(100000000, 3), columns=['x', 'y', 'z'])

    # Obtener las coordenadas del primer elemento
    punto_inicial = df.iloc[0]

    # Calcular la distancia euclidiana entre el primer elemento y cada uno de los otros elementos
    df['distancia'] = np.sqrt((df['x'] - punto_inicial['x'])**2 +
                              (df['y'] - punto_inicial['y'])**2 +
                              (df['z'] - punto_inicial['z'])**2)
    
    return df

def index(request):
    return render(request, 'index.html')

def sumar(request):
    print('starting op')
    start_time = time.time()
    df = crear_df_y_calcular_distancias()
    total_time = time.time() - start_time
    
    print(f"Total time {total_time} seconds.")


    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    resultado = num1 + num2 + len(df)
    
    return render(request, 'sumar.html', {'num1': num1, 'num2': num2, 'resultado': resultado})
