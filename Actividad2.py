#Diplomado Machine Learning - Corporación unificada nacional(CUN)
#Actividad 2: Cambio de divisas
#Autores: 
#   -Andrés Fernando Angarita Espitia 
#   -Edwin alfonso cruz caviedes
#   -Oscar Ivan Palomar Torres

import numpy as np

# Diccionario de tasas de cambio
tasasCambio = {
    ('USD', 'EUR'): 0.92,#Dolar a euro
    ('USD', 'GBP'): 0.80,#Dolar a libra
    ('USD', 'COP'): 4523,#Dolar a peso colombiano
    ('EUR', 'GBP'): 0.87,#Euro a libra
    ('EUR', 'COP'): 4895#Euro a peso colombiano
}

def calcularCambio(divOrigen, divDestino, cantidad):
    '''Calcula el cambio de divisas de una cantidad de una divisa a otra.'''
    if divOrigen == divDestino:
        return cantidad

    if (divOrigen, divDestino) in tasasCambio:
        tasa = tasasCambio[(divOrigen, divDestino)]
        cantidad_convertida = cantidad * tasa
        return cantidad_convertida
    elif (divDestino, divOrigen) in tasasCambio:
        tasa = tasasCambio[(divDestino, divOrigen)]
        cantidad_convertida = cantidad / tasa
        return cantidad_convertida
    else:
        return None

def calcular_ganancia(cantiOrigen, cantiDestino):
    '''Calcula la ganancia de una transacción de divisas.'''
    ganancia = cantiDestino - cantiOrigen
    return ganancia

# Divisas disponibles
divisas = {'USD', 'EUR', 'GBP', 'COP'}

#Ejecucion principal
print("Cambio de divisas")
print("Programa para calcular el cambio de divisas")
print("Divisas disponibles:")
for divisa in divisas:
    print(divisa)

divOrigen = input("Por favor ingrese la sigla de la divisa de origen en mayusculas: ")
divDestino = input("Por favor ingrese la sigla de la divisa de destino en mayusculas: ")
cantiOrigen = int(input("Por favor ingrese la cantidad de la divisa de origen: "))

try: 
    cantiDestino = calcularCambio(divOrigen, divDestino, cantiOrigen)
    ganancia_comprador = calcular_ganancia(cantiOrigen, cantiDestino)
    ganancia_vendedor = calcular_ganancia(cantiDestino, cantiOrigen)

    print(f"Cantidad original: {cantiOrigen} {divOrigen}")
    print(f"Cantidad convertida: {cantiDestino} {divDestino}")
    print(f"Ganancia para el comprador: {ganancia_comprador} {divDestino}")
    print(f"Ganancia para el vendedor: {ganancia_vendedor} {divOrigen}")
except:
    print("Error: Divisa no soportada")