A = [1, 2, 3, 4, 5]

caracter = input("introduzca un caracter")

while(caracter != 'x' and caracter != 'X'):
    A.append(caracter)
    caracter = input("introduzca un caracter")

print(A)
