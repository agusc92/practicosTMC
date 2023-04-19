A = [1, 2, 3, 4, 5]
B = [1, 2, 3, 4, 54]

def contenido(arr1, arr2):
    if all(elem in arr1 for elem in arr2):
        return "el conjunto esta contenido"
    else:
        return "el conjunto no esta contenido"

print(contenido(A, B))

def contenido2(arr1, arr2):
    result = 'el conjunto esta contenido'
    for i in arr2:
        if i not in arr1:
            result = 'el conjunto no esta contenido'
    
    return result

print(contenido2(A, B))
