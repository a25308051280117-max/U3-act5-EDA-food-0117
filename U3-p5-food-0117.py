import pandas as pd
import matplotlib.pyplot as plt
# Matias lopez NC 0117
# 1. Leer el archivo CSV comida pais india
df_food_india = pd.read_csv('india_food.csv')
print("\n--- DATOS LEÍDOS DESDE CSV,Comida india 0117 ---")
print(df_food_india)
print("\n--- mostrar nombre comida + ingredientes 0117 ---")
recetas = df_food_india[['name', 'ingredients']]
print(recetas)
print("\n--- tiempo de cocinado mostrar 10 registros con head 0117 ---")
nombre_y_hora = df_food_india[['name', 'cook_time']].head(10)
print(nombre_y_hora)
