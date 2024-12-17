def llegir_llista_paraules():
    l=[]
    a="a"
    while a!=".":
        a=input("Introdueix paraules: ")
        if a!=".":
            l.append(a)
    return l

b=llegir_llista_paraules()
print(b)