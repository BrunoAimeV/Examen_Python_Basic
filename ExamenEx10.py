import random

def menu():
    print("\nMenú Examen")
    print("Opcions:")
    print("1. Llegir una llista de Nombres.")
    print("2. Dir els números Senars.")
    print("3. Sumar números parells.")
    print("4. Cercar número dins una llista.")
    print("5. Llegir un número de paraules.")
    print("6. Donar les inicials d'una llista de paraules.")
    print("7. Números aleatoris.")
    print("8. Comparar llistes.")
    print("9. Veure les edats")
    
    opcio = int(input("Tria la teva opció: "))
    
    if opcio == 1:
        b = llegir_llista_paraules()
        print(b)
        
    elif opcio == 2:
        senars_llista()
        
    elif opcio == 3:
        b = senars_llista_sumar()
        print(f"La suma dels números parells és: {b}")
        
    elif opcio == 4:
        numero = int(input("Introdueix un número per cercar a la llista: "))
        resultado = cercar_numeros_llista([1, 2, 3, 4, 5, 6, 7, 8], numero)
        if resultado != -1:
            print(f"El número {numero} està a la posició {resultado}.")
        else:
            print("-1")
    
    elif opcio == 5:
        b = llegir_llista_paraules()
        print(f"La llista de paraules és: {b}")
    
    elif opcio == 6:
        b = llegir_llista_paraules()
        inicials = [paraula[0] for paraula in b]
        print(f"Les inicials de les paraules són: {''.join(inicials)}")
    
    elif opcio == 7:
        numeros_aleatoris = crear_llista_num_aleatoris()
        print(f"Números aleatoris: {numeros_aleatoris}")
    
    elif opcio == 8:
        llista1 = [input(f"Introdueix el {i+1} número de la llista 1: ") for i in range(5)]
        llista2 = [input(f"Introdueix el {i+1} número de la llista 2: ") for i in range(5)]
        resultats = comparar_llistes()
        print(f"Resultats de comparar les llistes: {resultats}")
    
    elif opcio == 9:
        edat1 = int(input("Introdueix la primera edat: "))
        edat2 = int(input("Introdueix la segona edat: "))
        major_edat(edat1, edat2)

def llegir_llista_paraules():
    l = []
    a = "a"
    while a != ".":
        a = input("Introdueix números: ")
        if a != ".":
            l.append(int(a))
    return l

def senars_llista():
    l = [1, 2, 3, 4, 5, 6, 7, 8]
    for n in l:
        if n % 2 == 1:
            print(n)

def senars_llista_sumar():
    l = [1, 2, 3, 4, 5, 6, 7, 8]
    suma = 0
    for n in l:
        if n % 2 == 0:
            suma = suma + n
    return suma

def cercar_numeros_llista(llista, numero):
    for i in range(len(llista)):
        if llista[i] == numero:
            return i
    return -1

def comparar_llistes():
    llista1 = ["Azul", "Rojo", "Amarillo", "Verde", "Naranja"]
    llista2 = ["Azul", "Rojo", "Naranja", "Gris", "Naranja"]
    resultats = []
    
    for i in range(len(llista2)):
        if llista2[i] == llista1[i]:
            resultats.append(2)
        elif llista2[i] in llista1:
            resultats.append(1)
        else:
            resultats.append(0)
    
    return resultats

def crear_paraula_llista():
    llista = ["Avión", "Barco", "Chocolate", "Dado"]
    primera_lletra = []
    for paraula in llista:
        primera_lletra.append(paraula[0])
    return primera_lletra

def crear_llista_num_aleatoris():
    l = []
    for _ in range(5):
        l.append(random.randint(1, 100))
    return l

def major_edat(edat1, edat2):
    if edat1 >= 18 and edat2 >= 18:
        print("Les dues edats són majors d'edat")
    elif edat1 >= 18 and edat2 < 18:
        print(f"{edat1} és major d'edat i {edat2} és menor d'edat")
    elif edat1 < 18 and edat2 >= 18:
        print(f"{edat1} és menor d'edat però {edat2} és major d'edat")
    else:
        print("Cap de les dues persones és major d'edat")

menu()