def cercar_numeros_llista(llista, numero):
    for i in range(len(llista)):
        if llista[i] == numero:
            return i 
    return 1

llista = [1, 2, 3, 4, 5, 6, 7, 8]
numero = int(input("Introduce un número para buscar en la lista: "))
resultado = cercar_numeros_llista(llista, numero)

if resultado != 1:
    print(f"El número {numero} está en la posición {resultado}.")
else:
    print("-1")