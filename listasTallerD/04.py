#Escribe una función en Python que reciba una lista de números enteros y devuelva una nueva lista que contenga solo los números que sean mayores que el promedio de los números en la lista original.

def promedioAlgo(lista):    
    return [ i for i in listaEnteros if i>sum(lista)/len(lista)]

listaEnteros=[1,2,3,4,5,6,7,8,9,10,11]
print(promedioAlgo(listaEnteros))


#Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura y elimine de la lista las asignaturas aprobadas. Al final el programa debe mostrar por pantalla las asignaturas que el usuario tiene que repetir.


cursos=['mat','fisica','quimica','lengua','dedo']
materiasPerdidas=[]

for i in cursos:
    x=float(input(f"que nota sacaste en {i}?: "))
    if x < 3.0:
        materiasPerdidas.append(i)
print(f"tienes que repetir estas materias: {materiasPerdidas}")        


lista2=[1,-1,2,-2,3,-3]
# s1,s2,s3 = sum(listaListas[0]), sum(listaListas[1]), sum(listaListas[2])
# print(f"La suma de {listaListas[0]} Es: {s1}, La suma de {listaListas[1]} Es: {s2}, La suma de {listaListas[2]} Es: {s3}")
subLista=[]

for i in range(len(lista2)):
    suma=0
    for j in range(i,len(lista2)):
        suma+=lista2[j]
        if suma == 0:
            subLista.append(lista2[i:j+1])

print(subLista)

