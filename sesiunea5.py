# #rezolvariTeme04
# #1.
# masini = ['Audi', 'Volvo', 'BMW' , 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
#
# #A.
# for idx in range(0,len(masini)):
#     print(f'Masina mea preferata este {masini}')
# #cu enumerate
# for idx, masina in enumerate(masini):
#     print(f'Masina mea preferata este {masina}')
#
# # C.
# i = 0
# while idx<len(masini):
#     print(f'Masina mea preferata este {masini[idx]}')
#     idx+=1
#
#
# #2.
# masini = ['Audi', 'Volvo', 'BMW' , 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
# for i in range(len(masini)):
#     if i == 0 or i == len(masini)-1:
#         masini[i] = masini[i].lower()
#     else:
#         masini[i] = masini[i].upper()
# print(masini)
########
###SESIUNEA 5

# F U N C T I O N S

# ce este o functie? - o zona de cod cu logica proprie
#         poate fi folosita si refolosita de cate ori aveam nevoie

# E o zona individuala de cod.

# Utilitatea princiala de a evita scrierea de cod duplicat

# Sintaxa D e f i n i r e Functie
# def nume_functie(eventuali_parametrii):
#     # codul aferent functiei
#
# # apelul se face cu:
# nume_functie(eventuali_parametrii)
# tipuri de functii BUILT-IN (print(), input(), type(), abs()...)

# Tipuri de functii EXPLICITE (scrise de noi)

def greeting():
    print("Hello!") # PYTHON LIMBAJ INTERPRETAT LINIE CU LINIE
print("Salut")
greeting()

# Vrem sa modificam sa ne salute personal, cu numele propriu..
# Ce facem?
# def greeting():
#     print("Hello, John")

# greeting()

# si daca vreau s o salut si pe Mary?
def greeting(name):
    print(f"Hello, {name}")

greeting("World")
greeting("Mary")

# altfel spus: PARAMETRII = DATE DE INTRARE ALE FUNCTIEI
# NU POATE FU CHEMAT DECAT IN INTERIORUL FUNCTIEI
# SCOP LOCAL - IN INTERIORUL FUNCTIEI
name = "John"
def greeting():
    global name
    print(f"Hello, {name}") # ii spunem ca 'name' e cel global,
                        # dar nu putem avea aacelasi parametru

greeting()
greeting()
print(name)

#Vrem sa scriem o functie care printeaza suma a 2 nr data ca argumente?

def sum_2(a,b):
    print(a+b)

sum_2(2,3)
sum_2(8,3)

#Acum ce am putea faca daca in programul "main" (in afara functiei sum_2),
# vrem sa:
# - printam rezultatul sumei: "Suma calculata este : <val_suma>"
# - folosim rezultatul sumei afisand: "Suma <val_suma> este para/impara"

def sum_2(a,b):
    return a+b
val_sum = sum_2(2,3)
print(f"Suma calculata este :{val_sum}")
if val_sum % 2 == 0:
    print(f"Suma {val_sum} este para")
else:
    print(f"Suma {val_sum} este impara")

def func():
    return 'alpha', 'beta'

t = func()
print(type(t))
print(t)
# putem lista, tupla, dict

# OBSERVAM DOUA TIPURI DE FUNCTII:
# - care returneaza
# - care nu returneaza

lst = [5,1,4,3,2]
# vrem sa sortam lista-doua optiuni
# sorted(lst) si lst.sort
sorted(lst) # sorteaza-return noua lista
print(lst)

lst.sort()# no return - modifica lista
print(lst)


##########
def greeting(name="World"):
    print(f'Hello, {name}')

# vom chema functia fara specificarea unui nume,
# caz in care ea sa foloseasca 'World'

# greeting()
# greeting("Universe")
#
# # Unde am mai vazut valori DEFAULT?
# d = {'a': 1, 'c':3}
# # Vrem sa luam val de la cheia 'b'
# print(d.get('b'))
# #Daca voiam sa punem "Cheia nu exista!"
# print(d.get('b', 'Cheia nu exista'))
# def greeting(age, name="World"):
#     print(f"Hello, my name is {name} and I am {age} years old")
#
# greeting(20, "John")
# greeting(4_000_000_000)

# ATENTIE PARAMETRII OPTIONALI TRB SITUATI DUPA CEI POZITIONALI
# def greeting(name="World", age): ###EROARE
#     print(f"Hello, my name is {name} and I am {age} years old")
# greeting(20)



# Vrem sa scriem o functie care aduna 3 numere si returneazza suma

def sum_4(a,b,c,d):
    return a+b+c+d

sum_4(1,2,3,4)

# Dar daca vrem sa adunam 10 nr? sau 100??
# Deja nu mai e amuzant codul....
# Exista ceva - *args - *kwargs / functii cu nr nedeterminat de argumente
#
# def sum_n(*args):
#     s = 0
#     for n in args:
#         s += n
#     return s
# print(sum_n(11,2,103,25,1,1111,53))
# print(sum_n(1,2,3))
#
# # putem apela si cu *tuple
# t = [15,3,2]
# print(sum_n(*t))
# l = [2,8,10,3]
# print(sum_n(*l))

# Avem dictionarul countries, vrem sa calculam suma populatiei tarilor din dict

# countries1 = {"Romania":19_500_000, "Moldova":4_000_000}
def sum_of_population(**kwargs): # args se evalueaza ca un dict
    s = 0
    for key in kwargs:
        s += kwargs[key]
    return s
countries1 = {"Romania":19_500_000, "Moldova":4_000_000}
print(sum_of_population(**countries1))

def sum_of_Romania(**kwargs):
    print(kwargs['Romania'])
####PUTEM SI ASA::
sum_of_Romania(Romania=19_500_000, Moldova=4_000_000)

#Vrem sa salutam tara data ca argument pozitional,
# si sa calculam suma a n nr date ca args optionale
# impreuna cu populatiile argumentelor keyword
#########
# C05_EX01: Vrem sa salutam tara data ca argument pozitional si sa calculam suma a n numere date ca argumente
# optionale impreuna cu populatiile argumentelor keyword
# def greet_and_sum_of_n_numers(country_name, *args, **kwargs):

    # greet_and_sum_of_n_numers("Romania", 100, 11, 1, Romania=19_500_000, Moldova=4_000_000)
# ar trebui sa returneze: 23500111
def greet_and_sum_of_n_numers(country_name, *args, **kwargs):
    print(f"Hello {country_name}")
    s = 0
    for n in args:
        s = s + n
    for key in kwargs:
        s = s + kwargs[key]
    return s
rezultat =greet_and_sum_of_n_numers("Romania", 100, 11, 1, Romania=19_500_000, Moldova=4_000_000)
print(rezultat)

#####EXCEPTII

# exceptiile sunt niste evenimente ce apar in cod
# si intrerup executia normala
# exceptia poate fi si o eroare
# ar trebui sa ni le inchipuim ca pe niste obiecte care rep o eroare specifica

# print(some_var_name)
#####NAME-ERROR
######ZeroDivisionError #print(3/0)
#ATRIBUTEerror
# lst = [1,2,3,4]
#lst.addd
#######
#lst = [1,2,3,4]
###INDEX-ERROR
#######
# import some_fake_module -- ImportError!!
# d {1, 2:1}
###KeyError
# n=int(input(dati un nr)
## ValueError
# print("string"+3)
##TYPE-ERROR


#putem anticipa cand apar exceptii si sa le facem handling
# exista keywords specifice exceptiilor:

# try - except - else - finally
# raise
# nr = int(input("Introduceti un nr: "))
# nr = int(nr)
#
# nr = int(input("Introduceti un nr: "))
# try:
#     nr = int(nr)
#     print(nr)
# except ValueError:
#     print("Nu ati introdus un numar!")
# print("Exec codului continue aici")
#se incearca executia blocului try, daca nu apare exceptie blocul except nu se executa
# daca in schimb apare o eraore, blocul try este intrerupt si se executa blocul except

# iar apoi se continua cu restul codului din afara try-except
# sintaxa generala pt exceptii:
# try:
    #aici avem executia normala, fara erori
# except:
    #aici se intra in cazul in care apar erori, intrerupand try-ul
    #pe blocul except se face handlingla eventuale erori ce pot aparea
# else:
    #bloc care se executa in continuarea blocului try,
    # in cazul in care nu a aparut nicio exceptie
# finally:
    # bloc care se executa intotdeauna indiferent ca avem sau nu errori

# ce afiseaza codul urmator?

# try:
#     if aha:
#         print(1)
# except:
#     print(2)
# else:
#     print(3)
# finally:
#     print(4)
#
# try:
#     x = int(input("Alege un numar: "))
#     print(qwerty/0)
# except NameError:
#     print("Am prins o exceptie NameError")
# except (ZeroDivisionError, NameError):
#     print("Am prins o exceptie ZeroDivisionError, NameError")
# except:
#     print("Am prins o alta exceptie")
