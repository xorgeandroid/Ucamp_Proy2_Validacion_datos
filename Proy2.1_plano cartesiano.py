
import matplotlib.pyplot as plt
import os

# Solicitar las coordenadas (x,y) por el usuario
x = float(input("Ingrese la coordenada de X: "))
y = float(input("Ingrese la coordenada de Y: "))

# Verificar que no sean 0 las coordenadas
if x == 0 or y == 0:
    print("Las coordenadas deben ser diferentes de 0.")
else:
    # identificar en qué cuadrante se encuentran los valores ingresados y de manera gráfica con color.
    if x > 0 and y > 0:
        print("El punto se encuentra en el cuadrante I.")
        plt.scatter(x, y, color="green")
    elif x < 0 and y > 0:
        print("El punto se encuentra en el cuadrante II.")
        plt.scatter(x, y, color="blue")
    elif x < 0 and y < 0:
        print("El punto se encuentra en el cuadrante III.")
        plt.scatter(x, y, color="red")
    else:
        print("El punto se encuentra en el cuadrante IV.")
        plt.scatter(x, y, color="yellow")

    # Configurar los ejes del plano cartesiano
    plt.axhline(y=0, color="black")
    plt.axvline(x=0, color="black")
    plt.xlim(-10, 10)
    plt.ylim(-10, 10)

    # Mostrar el plano cartesiano con el punto graficado
    plt.show()
    os.system('pause')
