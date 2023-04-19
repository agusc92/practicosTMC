def pedirLista(curso):
    nombre = input('introduzca el nombre de un alumno de '+curso)
    aux = []
    while nombre != 'x' and nombre != 'X':
        aux.append(nombre)
        nombre = input('introduzca el nombre de un alumno de '+curso)
    return aux


primario = pedirLista('primario')
secundario = pedirLista('secundario')

def auxFunction(arr, aux):
    #devuelve un array los valores no repetidos
    for i in arr:
        if i not in aux:
            aux.append(i)
    return aux

def listado(arr1, arr2):
    aux = []
    aux = auxFunction(arr1, aux)

    aux = auxFunction(arr2, aux)

    return aux

# print(listado(primario, secundario))


def identificaRepetidos(arr1, arr2):
    aux = arr1.copy()
    aux2 = []
    for i in arr2:
        aux.append(i)
    for i in listado(arr1, arr2):
        aux.remove(i)
    for i in aux:
        if i not in aux2:
            aux2.append(i)
    return aux2

def noRepetidos(arr1, arr2):
    aux=[]
    for i in arr1:
        if i not in arr2:
            aux.append(i)
    return aux


print('la lista de los alumnos es: ')
print(listado(primario, secundario))
print('los nombres repetidos son: ')
print(identificaRepetidos(primario, secundario))
print('los nombres de primario que no se repiten en secundario son: ')
print(noRepetidos(primario, secundario))
print('los nombres de secundario que no se repiten en primario son: ')
print(noRepetidos(secundario, primario))

