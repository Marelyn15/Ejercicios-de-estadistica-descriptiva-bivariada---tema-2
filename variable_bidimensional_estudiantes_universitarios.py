#Datos

#ID del estudiante
Id = []
for i in range(1,21):
    Id.append(i)
#Genero y categoria (ejemplo)
gc = []
for index in range(1,21):
    if index <= 4:
        gc.append(['F','Msc'])
    elif index == 5:
        gc.append(['F', 'PhD'])
    elif index >= 6 and index < 15:
        gc.append(['M', 'Msc'])
    else:
        gc.append(['M', 'PhD'])

#Colocando en un diccionario
Datos = dict(zip(Id,gc))

#Cantidad total de estudiantes
cantidad_total = len(Id)
#===================================================
#Cantidad total de estudiantes femeninos y masculinos
masculinos = []
femenino = []
for i in Datos.values():
    if i[0] == 'M':
        masculinos.append(i[0])
    else:
        femenino.append(i[0])

masculinos = masculinos.count('M')
femenino = femenino.count('F')

porcentaje_femeninos = round(femenino/cantidad_total,2)
porcentaje_masculinos = round(masculinos/cantidad_total,2)


#Conclusion 1
print(f"De la cantidad total de estudiantes hay {masculinos} hombres representando el {porcentaje_masculinos * 100}% de todos los estudiantes masculinos y hay un total de {femenino} mujeres representando el {porcentaje_femeninos * 100}% de todos los estudiantes femeninos. En total hay {cantidad_total} estudiantes.")

#Porcentaje de mujeres y hombres que están estudiando alguna carrera
carrera_feminas = []
carrera_masculinos = []

for i in Datos.values():
    if i[0] == 'F':
        carrera_feminas.append(i[1])
    else:
        carrera_masculinos.append(i[1])

carrera_feminas_Msc = carrera_feminas.count('Msc')
carrera_feminas_PhD = carrera_feminas.count('PhD')

carrera_masculinos_Msc = carrera_masculinos.count('Msc')
carrera_masculinos_PhD = carrera_masculinos.count('PhD')

porcentaje_carrera_feminas_Msc = round(carrera_feminas_Msc/femenino,2)
porcentaje_carrera_feminas_PhD =  round(carrera_feminas_PhD/femenino,2)

porcentaje_carrera_masculinos_Msc = round(carrera_masculinos_Msc/masculinos,2)
porcentaje_carrera_masculinos_PhD = round(carrera_masculinos_PhD/masculinos,2)


#Conclusion 2
print(f"Del total de las femininas ({femenino}) hay {carrera_feminas_Msc} mujeres que están haciendo Maestría representando el {porcentaje_carrera_feminas_Msc * 100}% de las mujeres y el total de feminas que están haciendo un doctorado hay {carrera_feminas_PhD}, representando un {porcentaje_carrera_feminas_PhD * 100}%.")

print(f"Del total de las masculino ({masculinos}) hay {carrera_masculinos_Msc} hombres que están haciendo Maestría representando el {porcentaje_carrera_masculinos_Msc * 100}% de las hombres y el total de masculinos que están haciendo un doctorado hay {carrera_masculinos_PhD}, representando un {porcentaje_carrera_masculinos_PhD * 100}%.")

#Respecto al total:
porcentaje_carrera_feminas_Msc_RT = round(carrera_feminas_Msc/cantidad_total,2)
porcentaje_carrera_feminas_PhD_RT =  round(carrera_feminas_PhD/cantidad_total,2)

porcentaje_carrera_masculinos_Msc_RT = round(carrera_masculinos_Msc/cantidad_total,2)
porcentaje_carrera_masculinos_PhD_RT = round(carrera_masculinos_PhD/cantidad_total,2)

#Conclusion 3
print(f"Del total de las femininas que estudian Maestría hay {carrera_feminas_Msc} que representa el {porcentaje_carrera_feminas_Msc_RT * 100}% de todos los estudiantes y el total de feminas que están haciendo un doctorado hay {carrera_feminas_PhD}, representando un {porcentaje_carrera_feminas_PhD_RT * 100}%.")

print(f"Del total de los masculinos que estudian Maestría hay {carrera_masculinos_Msc} que representa el {porcentaje_carrera_masculinos_Msc_RT * 100}% de todos los estudiantes y el total de masculinos que están haciendo un doctorado hay {carrera_masculinos_PhD}, representando un {porcentaje_carrera_masculinos_PhD_RT * 100}%.")

print(f"El total de los estudiantes que hacen una maestría son {carrera_feminas_Msc + carrera_masculinos_Msc} que representa el {(porcentaje_carrera_masculinos_Msc_RT + porcentaje_carrera_feminas_Msc_RT) * 100}%")

print(f"El total de los estudiantes que hacen una doctorado son {carrera_feminas_PhD + carrera_masculinos_PhD} que representa el {round((porcentaje_carrera_masculinos_PhD_RT + porcentaje_carrera_feminas_PhD_RT) * 100,1)}%")


 #Conclusion 4 

print(f"La distribución porcentual de estudiantes según genero es {round((carrera_feminas_Msc /(carrera_feminas_Msc + carrera_masculinos_Msc)),2)*100}% para las feminas de mastria y {round((carrera_masculinos_Msc/ (carrera_feminas_Msc + carrera_masculinos_Msc)),2)*100}% para los masculinos")

print(f"La distribución porcentual de estudiantes según genero es {round((carrera_feminas_PhD/(carrera_feminas_PhD + carrera_masculinos_PhD)),2)*100}% para las feminas de doctorado y {round((carrera_masculinos_PhD/ (carrera_feminas_PhD + carrera_masculinos_PhD)),2)*100}% para los masculinos")









    
