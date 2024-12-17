def crear_paraula_llista():
    llista = ["Avión", "Barco", "Chocolate", "Dado"]
    primera_lletra = []
    for paraula in llista:
        primera_lletra.append(paraula[0])
    return primera_lletra

b = crear_paraula_llista()
print(b)