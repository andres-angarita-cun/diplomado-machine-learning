#Diplomado Machine Learning - Corporación unificada nacional(CUN)
#Actividad 3: ETL
#Autores: 
#   -Andrés Fernando Angarita Espitia 
#   -Edwin alfonso cruz caviedes
#   -Oscar Ivan Palomar Torres

import pandas as pd
from sklearn.datasets import fetch_openml
from sqlalchemy import create_engine

# Paso 1: Extracción de datos de digitos escritos a mano
mnist = fetch_openml('mnist_784')

# Paso 2: Transformación de datos para la facilidad de tratamiento
df = pd.DataFrame(data=mnist['data'], columns=mnist['feature_names'])
df['target'] = mnist['target']

# Paso 3: Carga de datos en la base de datos SQL
# Establece la conexión con la base de datos
engine = create_engine('mysql://root:1234@localhost/mnist_db')

# Carga el DataFrame en la tabla "mnist_data" de la base de datos
df.to_sql('mnist_data', engine, if_exists='replace', index=False)

# Cierra la conexión
engine.dispose()

# Paso 4: Análisis exploratorio de datos 
print("Información del conjunto de datos:")
print(df.info())

print("Estadísticas descriptivas del conjunto de datos:")
print(df.describe())

print("Primeras filas del conjunto de datos:")
print(df.head())
# ¡Fin del proceso ETL!
