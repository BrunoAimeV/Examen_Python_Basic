def senars_llista():
    l=[1,2,3,4,5,6,7,8]
    suma=0
    for n in l:
        if n%2==0:
            suma = suma + n
    return suma
b=senars_llista()
print(b)