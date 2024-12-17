def llegir_llista_enters():
    l=[]
    a="a"
    while a!=".":
        a=input("Escriu un nombre: ")
        if a!=".":
            l.append(int(a))
    return l
b=llegir_llista_enters()
print(b)