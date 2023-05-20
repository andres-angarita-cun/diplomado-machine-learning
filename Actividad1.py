#Diplomado Machine Learning - Corporación unificada nacional(CUN)
#Actividad 1: Empresas de papas fritas
#Autores: 
#   -Andrés Fernando Angarita Espitia 
#   -Edwin alfonso cruz caviedes
#   -Oscar Ivan Palomar Torres

#Librerias
import numpy as np

#declarar vector
T = 5  # Días de la semana (lunes a viernes)
N = 3  # Número de referencias

ventas = np.zeros((T, N), dtype=int)

def captura_ventas():
    '''Captura las ventas de las referencias para cada día de la semana'''
    for i in range(T):
        for j in range(N):
            ventas[i, j] = int(input(f"Digite el valor de ventas para la referencia {j+1} en el día {i+1}: "))
          
def mostrar_ventas():
    '''Muestra las ventas de las referencias para cada día de la semana'''
    for i in range(T):
        for j in range(N):
            print(f"Venta para la referencia {j+1} en el día {i+1}: {ventas[i, j]}")

def venta_mayor():
    '''Muestra la venta mayor de las referencias para cada día de la semana'''
    max_valor = np.max(ventas)
    indices = np.where(ventas == max_valor)
    dia = indices[0][0]
    referencia = indices[1][0]
    print(f"La venta mayor es {max_valor} en el día {dia+1} para la referencia {referencia+1}")

def venta_menor():
    '''Muestra la venta menor de las referencias para cada día de la semana'''
    min_valor = np.min(ventas)
    indices = np.where(ventas == min_valor)
    dia = indices[0][0]
    referencia = indices[1][0]
    print(f"La venta menor es {min_valor} en el día {dia+1} para la referencia {referencia+1}")


def titulo():
    print("Empresas de papas fritas")

def salir():
    print("Bye")

def main():
    '''Función principal'''
    titulo()
    captura_ventas()
    mostrar_ventas()
    venta_mayor()
    venta_menor()
    salir()

#Bloque principal
main()