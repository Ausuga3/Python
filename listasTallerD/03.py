#Hacer un algoritmo que nos pida la información de 5 empleados: Nombre, apellido, horas trabajadas y edad. El sistema nos debe mostrar cuánto ganó cada uno al mes, y cuántas horas trabajaron en promedio al mes. Nota: Hora=$6000.

nombres =[]
apellidos=[]
edad=[]
horasTrabajadas=[]
valorHora=6000

for i in range(5):
    nombre=input("Ingrese su nombre: ").capitalize()
    apellido=input("Ingrese su apellido: ").capitalize()
    edad1=int(input("Ingrese su edad: "))
    horasTrabajadaEmpleado=float(input("Cuantas horas trabajaste?: "))

    nombres.append(nombre)
    apellidos.append(apellido)
    edad.append(edad1)
    horasTrabajadas.append(horasTrabajadaEmpleado)

totalHoras = sum(horasTrabajadas)
promedio = totalHoras / len(horasTrabajadas)    

for i in range(len(nombres)):
    salario = horasTrabajadas[i] * valorHora
    print(f"{nombres[i]} {apellidos[i]} ganó ${salario} al mes.")

print(f"En promedio, los empleados trabajaron {promedio} horas al mes.")


