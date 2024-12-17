def major_edat(edat1, edat2):
    if edat1 >= 18 and edat2 >= 18:
        print("Les dues edats són majors d'edat")
    elif edat1 < edat2 and edat2 >= 18:
        print(f"{edat1} és menor d'edat però {edat2} és major d'edat")
    else:
        print("Cap de les dues persones és major d'edat")

edat1=int(input("Introdueix la primera edat: "))
edat2=int(input("Introdueix la segona edat: "))

major_edat(edat1, edat2)
