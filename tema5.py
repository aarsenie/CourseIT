# 1. Functie care sa calculeze si sa returneze suma a 2 numere

def sum_2(a,b):
    print(a+b)

sum_2(2,6)

# 2. Functie care sa returneze TRUE daca un numar este par, FALSE pt impar

def par_impar(a):
    if a % 2 ==0:
        return True
    else:
        return False
print(par_impar(7))

# 3. Functie care returneaza numarul total de caractere din numele tau complet.
# (nume, prenume, nume_mijlociu)

def nume_complet(a,b,c):
    return(len(a + b + c))
print(nume_complet("Arsenie","Alexandra","Maria"))

# 4. Functie care returneaza aria dreptunghiului
def aria_dreptunghiului(a,b):
    return (a * b)
print(aria_dreptunghiului(4,6))

# 5. Functie care returneaza aria cercului
def aria_cercului(raza):
    return (3.14 * raza * raza)
print(aria_cercului(4))
# 6. Functie care returneaza True daca un caracter x se gaseste intr-un string dat. Fasle daca nu
def bool_caracter(x, word):
    if x in word:
        return True
    else:
        return False
print(bool_caracter('b',"Buna siua"))

# 7. Functie fara return, primeste un string si printeaza pe ecran:
# Nr de caractere lower case este x
# Nr de caractere upper case exte y
def lower_upper(s):
        u = sum(1 for i in s if i. isupper())
        l = sum(1 for i in s if i. islower())
        print("Nr de caractere lower case este : %s , Nr de caractere upper case este: %s" % (u,l))
lower_upper("Buna siua dragii mei")

# 8. Functie care primeste o LISTA de numere
# si returneaza o LISTA doar cu numerele pozitive

def positive_number(NumList):

    NumarPozitiv = []
    for i in NumList:
        if i >= 0:
            NumarPozitiv.append(i)

    return NumarPozitiv


NumList =[1, -2, 3, -4]
print(positive_number(NumList))

# 9. Functie care nu returneaza nimic. Primeste 2 numere si PRINTEAZA
# Primul numar x este mai mare decat al doilea nr y
# Al doilea nr y este mai mare decat primul nr x
# Numerele sunt egale.

def doua_numere(x,y):
    if x > y:
        print(f"Primul numar {x} este mai mare decat al doilea nr {y}")
    elif x < y:
        print(f"Al doilea nr {y} este mai mare decat primul nr {x}")
    else:
        print(f"Numerele sunt egale")

doua_numere(4,3)

#
# 10. Functie care primeste un numar si un set de numere.
# Printeaza ‘am adaugat numarul nou in set’ + returneaza True
# Sau Printeaza ‘nu am adaugat numarul in set. Acesta exista deja’ + returneaza False #in/find

def s1(x, SetNr):
    if x in SetNr:
        print("Nu am adaugat numarul in set. Acesta exista deja")
        return True
    else:
        SetNr.add(x)
        print("Am adaugat numarul nou in set")
        return False

SetNr = {1, 2, 3}
x = 4
print(s1(x, SetNr))

#16.

