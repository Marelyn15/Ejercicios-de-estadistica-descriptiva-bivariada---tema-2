import math
import pandas as pd

"""
| Y/X | 0 | 2 | 4 |
| --- |---|---|---|
|  1  | 2 | 1 | 3 |
|  2  | 1 | 4 | 2 |
|  3  | 2 | 0 | 0 |
"""

#Creamos la tabla de contingencia
tabla_contingencia = {
    0:{1:2,2:1,3:2}, #Frecuencia X = 0
    2:{1:1,2:4,3:5}, #Frecuencia X = 2
    4:{1:3,2:2,3:0}  #Frecuencia X = 4
}

#Convirtiendo en DataFrame
df = pd.DataFrame([
    {'x_i':x,'y_i':y, 'n_i':n}
    for x, filas in tabla_contingencia.items()
    for y, n in filas.items()
])
print(df)

#Entramos todo en variables distintas:
x = []
for i in df['x_i']:
    x.append(i)
print(x)

y = []
for i in df['y_i']:
    y.append(i)
print(y)

n = []
for i in df['n_i']:
    n.append(i)
print(n)

#Ejemplo: 
def regresion_lineal_agrupados(x,y,ni):
    #Resumen datos
    print(f"Estos son los datos de entrada: x = {x} e y = {y}, y la frecuencia absoluta (ni) es: {ni}")
    cantidad_registros = sum(ni) #n
    print(f"Su cantidad de registro para ambos es {cantidad_registros}")

    #Multiplicando cada elemento de x por cada elemento de la frecuencia absoluta
    x_por_ni = []
    for index, numero in enumerate(x):
        x_por_ni.append(numero * ni[index])

    #Multiplicando cada elemento de y por cada elemento de de la frecuencia absoluta
    y_por_ni = []
    for index, numero in enumerate(y):
        y_por_ni.append(numero * ni[index])

    #Total de los valores multiplicados
    total_x = sum(x_por_ni)
    total_y = sum(y_por_ni)
    print(f"El total de x por la frecuencia absoluta (ni) es: {total_x} y el total de y por la frecuencia absoluta (ni) es: {total_y}")

    #Multiplicando cada elemento de x por cada elemento de y y por ni
    xi_yi_ni = []
    for index, numero in enumerate(x):
        xi_yi_ni.append(numero * y[index] * ni[index])

    #La sumatoria final de todos esos elementos
    total_xi_yi_ni = sum(xi_yi_ni)
    print(f"Esto es la multiplicacion resultante para cada elemento de xi,yi,ni: {xi_yi_ni} y la sumatoria es: {total_xi_yi_ni}")

    #Media
    media_x = total_x/cantidad_registros
    media_y = total_y/cantidad_registros
    print(f"esta es la media de x: {media_x} y esta es la media de y: {media_y}")

    #Covarianza de x e y
    covarianza = round((total_xi_yi_ni/cantidad_registros) - media_x * media_y,2)
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

    x_cuadrado_ni = []
    for indice, numero in enumerate(x):
        x_cuadrado_ni.append((numero*numero) * ni[indice])

    y_cuadrado_ni = []
    for indice, numero in enumerate(y):
        y_cuadrado_ni.append((numero*numero)* ni[indice])

    #Sumatoria de los elementos al cuadrado
    total_x_cuadrado = sum(x_cuadrado)
    total_y_cuadrado = sum(y_cuadrado)
    total_x_cuadrado_ni = sum(x_cuadrado_ni)
    total_y_cuadrado_ni = sum(y_cuadrado_ni)

    #Desviacion estandar
    desviacion_x = round(math.sqrt((total_x_cuadrado_ni/cantidad_registros) - (media_x * media_x)),2)
    desviacion_y = round(math.sqrt((total_y_cuadrado_ni/cantidad_registros) - (media_y * media_y)),2)
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

    #Coeficiente de determinacion
    coeficiente_determinacion = (correlacion * correlacion)
    print(f"Este es el coeficiente de determinacion: {coeficiente_determinacion * 100}%")

    """
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
    """
    
regresion_lineal_agrupados(x,y,n)