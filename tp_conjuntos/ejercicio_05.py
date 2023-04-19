A = [1, 2, 3, 4, 5]
B = [2, 4, 6, 8,]


def AUB(arr1, arr2):
    aux = arr1.copy()
    for i in arr2:
        aux.append(i)

    return aux


# print(AUB(A, B))


def AnB(arr1, arr2):
    aux = []
    for i in arr1:
        if i in arr2:
            aux.append(i)

    return aux


#print(AnB(A, B))


def AmenosB(arr1, arr2):
    aux = arr1.copy()
    for i in arr2:
        if i in arr1:
            aux.remove(i)
    
    return aux

#print(AmenosB(A, B))
print(AmenosB(B, A))     
