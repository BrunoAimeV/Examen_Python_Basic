import random

def crear_llista_num_aleatoris():
    l=[]
    for _ in range(5):
        l.append(random.randint(1,100))
    return l

print(crear_llista_num_aleatoris())