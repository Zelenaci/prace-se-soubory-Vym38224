from random import randint, choice

def menu():
    print("""
Co chceš dělat?
1) Převést na malá písmena.
2) Nahrazení znaků jiným znakem.
3) Statistika výskytu jednotlivých znaků v souboru.
4) Generování náhodného textu.
""")
    volba = input("Zadej svoji volbu: ")
    return volba
    
if __name__ == "__main__":
    volba = menu()


def prevod():
    try:
        f1 = open(input("Zadej název vstupního souboru: "),"r")
    except FileNotFoundError:
        print("Soubor nebyl nalezen")

    try:
        f2 = open(input("Zadejte název výstupního souboru: "),"w")
    except FileNotFoundError:
        print("Soubor nebyl nalezen")

    text = f1.read().lower()
    f2.write(text)
    
    f1.close()
    f2.close()

if volba == "1":
    prevod()


def nahrada():
    try:
        f1 = open(input("Zadej název vstupního souboru: "),"r")
    except FileNotFoundError:
        print("Soubor nebyl nalezen")

    try:
        f2 = open(input("Zadejte název výstupního souboru: "),"w")
    except FileNotFoundError:
        print("Soubor nebyl nalezen")

    while True:
        znak = f1.read(1)
        if znak == "":
            break
        if znak == "C":
            znak = "X"
        f2.write(znak)

    text = f1.read()
    f2.write(text)
    
    f1.close()
    f2.close()

if volba == "2":
    nahrada()


def statistika():
    try:
        f1 = open(input("Zadej název vstupního souboru: "),"r")
    except FileNotFoundError:
        print("Soubor nebyl nalezen")

    while True:
        pismeno = f1.read(1)
        if pismeno =="":
            break
        
        if pismeno.isalpha():
            if pismeno not in pocet.keys():
                pocet[pismeno] = 1
            else:
                pocet[pismeno] += 1
    f1.close()
    nej = max(pocet.values())
    for key in sorted(pocet.keys()):
        print(key, pocet[key])
    
    try:
        f2 = open(input("Zadejte název výstupního souboru: "),"r")
    except FileNotFoundError:
        print("Soubor nebyl nalezen")
    
    while True:
        pismeno = f2.read(1)
        if pismeno =="":
            break
        
        if pismeno.isalpha():
            if pismeno not in pocet.keys():
                pocet[pismeno] = 1
            else:
                pocet[pismeno] += 1
    f2.close()
    nej = max(pocet.values())
    for key in sorted(pocet.keys()):
        print(key, pocet[key])

pocet = {}

if volba == "3":
    statistika()


if volba == "4":
    try:
        f2 = open(input("Zadejte název výstupního souboru: "),"w")
    except FileNotFoundError:
        print("Soubor nebyl nalezen")

samohlasky = "aeiyou"
souhlasky = "qwrtpsdfghjklzxcvbnm"

def slovo(minznak = 1 , maxznak = 7):
    vysledek = ""
    pocet = randint(minznak, maxznak)

    for i in range(pocet):
        if i % 2 == 0:
            vysledek = vysledek + choice(samohlasky)
        else:
            vysledek = vysledek + choice(souhlasky)
    return vysledek

pocet_slov = int(input("Zadejte počet slov: "))

def veta(minslov = pocet_slov, maxslov = pocet_slov):
    vysledek2 = ""
    for i in range(randint(minslov, maxslov)):
        vysledek2 = vysledek2 + slovo() + " "
    return vysledek2.capitalize()[0:-1] + "."
 
veta = veta()
f2.write(veta)




    




        
        




















    











    
    



        
    

    

       


    

    
    