import random
import math
"""
x = []

for i in range(1,11):
    x.append(random.randrange(1,10))

print(x)


y = []

for i in range(1,11):
    y.append(random.randrange(1,10))

print(y)
"""

#Ejemplo: 
x = [2,3,4,4,5,6,6,7,7,8,10,10]
y = [1,3,2,4,4,4,6,4,6,7,9,10]

def regresion_lineal_no_agrupados(x,y):
    print(f"Estos son los datos de entrada: x = {x} e y = {y}")
    cantidad_registros = len(x)
    print(f"Su cantidad de registro para ambos es {cantidad_registros}")
    total_x = sum(x)
    total_y = sum(y)
    print(f"El total de x es: {total_x} y el total de y es: {total_y}")

    #Multiplicando cada elemento de x por cada elemento de y
    x_por_y = []
    for index, numero in enumerate(x):
        x_por_y.append(numero * y[index])

    #La sumatoria final de todos esos elementos
    total_x_por_y = sum(x_por_y)
    print(f"El total de x * y es: {total_x_por_y}")

    #Media
    media_x = total_x/cantidad_registros
    media_y = total_y/cantidad_registros
    print(f"esta es la media de x: {media_x} y esta es la media de y: {media_y}")

    #Covarianza de x e y
    covarianza = round((total_x_por_y/cantidad_registros) - media_x * media_y,2)
    print(f"La covarianza es: {covarianza}")

    #Signo de la covarianza
    if covarianza > 0:
        print("Covarianza es positiva")
    else: 
        print("Covarianza es negativa")

    #Correlación: 
    #Convirtiendo cada elemento de las variables al cuadrado
    x_cuadrado = []
    for i in x:
        x_cuadrado.append(i*i)

    y_cuadrado = []
    for i in y:
        y_cuadrado.append(i*i)

    #Sumatoria de los elementos al cuadrado
    total_x_cuadrado = sum(x_cuadrado)
    total_y_cuadrado = sum(y_cuadrado)

    #Desviacion estandar
    desviacion_x = round(math.sqrt((total_x_cuadrado/cantidad_registros) - (media_x * media_x)),2)
    desviacion_y = round(math.sqrt((total_y_cuadrado/cantidad_registros) - (media_y * media_y)),2)
    print(f"Esta es la desviacion estandar de x {desviacion_x} y esta es la desviacion estandar y {desviacion_y}")

    #Desviacion estándar
    correlacion = round(covarianza / (desviacion_x * desviacion_y),2)
    print(f"La correlación es : {correlacion}")

    #Regresion lineal: 
    varianza_x = round((total_x_cuadrado/cantidad_registros) - (media_x * media_x),2)
    print(f"Varianza de x es el total de x al cuadrado ({total_x_cuadrado}) entre la cantidad de registros ({cantidad_registros}) menos la media de y ({media_x}) al cuadrado ({(media_x * media_x)}) es igual a {varianza_x}")

    varianza_y = round((total_y_cuadrado/cantidad_registros) - (media_y * media_y),2)
    print(f"Varianza de y es el total de y al cuadrado ({total_y_cuadrado}) entre la cantidad de registros ({cantidad_registros}) menos la media de y ({media_y}) al cuadrado ({(media_y * media_y)}) es igual a {varianza_y}")

    print(f"Esta es la varianza de x {varianza_x} y esta es la varianza de y {varianza_y}")

    #Recta de y sobre x
    numeros_multiplicar_x = [1,-1*(media_x)]
    recta_y_sobre_x = []
    mult_x = round((covarianza / varianza_x),3)
    print(f"covarianza entre varianza de x es: {mult_x}")

    for numero in numeros_multiplicar_x:
        recta_y_sobre_x.append(numero * mult_x)

    recta_y_sobre_x[1] = round((recta_y_sobre_x[1] + media_y),2)
    print(f"La recta de y sobre x es: {recta_y_sobre_x}")


    #Recta de x sobre y
    numeros_multiplicar_y = [1,-1*(media_y)]
    print(numeros_multiplicar_y)
    recta_x_sobre_y = []
    mult_y = round((covarianza/varianza_y),3)

    print(f"La covarianza ({covarianza}) entre la varianza de y ({varianza_y}) es: {mult_y}")

    for numero in numeros_multiplicar_y:
        recta_x_sobre_y.append(numero * mult_y)
    recta_x_sobre_y[1] = round((recta_x_sobre_y[1] + media_x),2) 
    print(f"La recta de x sobre y es: {recta_x_sobre_y}")

    #Conclusion:
    print(f"La recta de y sobre x es igual a Y = {recta_y_sobre_x} y la recta de x sobre y es igual a X = {recta_x_sobre_y}")

    #Coeficiente de determinacion
    coeficiente_determinacion = (correlacion * correlacion)
    print(f"Este es el coeficiente de determinacion: {coeficiente_determinacion * 100}%")
    
regresion_lineal_no_agrupados(x,y)