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


b=comparar_llistes()
print(b)