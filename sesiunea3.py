# OBSERVATII:

# - trebuie sa invatam sa scriem cod CURAT si ORDONAT
# - indentare se face fie cu 4 spatii, fie cu tab

# EX 2: Verifica si afiseaza daca este de numar natural sau nu
#
# x = -1
# if x >= 0:
#     print('Numarul este natural')
# else:
#     print("Numarul nu este natural")
#
# x = 3.5 # numar natural = numar intreg mai mare sau egal cu 0
# if x >= 0 and isinstance(x, int):
#     print('Numarul este natural')
# else:
#     print("Numarul nu este natural")
#
# # # 4. Verifica si afiseaza daca x este intre -2 si 13
# #
# # x = float(input("Introdu un numar:"))
# # if x in range (-2, 13):
# #     print ("Adevarat")
# # else:
# #     print("Fals")
# if x >= - 2 and x <= 13: PENTRU A ACCEPTA SI NUMERELE DOI INDICI (3.5)
#     print(True)
#   else:
#       print(False)

# # # 5. Verifica si afiseaza daca diferenta intre x si y este mai mica de 5
# x = int(input('Introduceti x: '))
# y = int(input('Introduceti y: '))
# diff1 = x - y
# diff2 = y - x
# if diff1 < 5 or diff2 < 5:
#     print("Diferenta e mai mica decat 5")
# else:
#     print("Diferenta e mai mare decat 5")
# #INCOMPLETA
# ######
# x = int(input('Introduceti x: '))
# y = int(input('Introduceti y: '))
# if x > y:
#     diff = x - y
# else:
#     diff = y - x
# print(diff)
# if diff < 5:
#     print("Diferenta e mai mica decat 5")
# else:
#     print("Diferenta e mai mare sau egale cu 5")
# ###########################
#
# # v2
# if abs(x - y) < 5:
#     print("Diferenta e mai mica decat 5")
# else:
#     print("Diferenta e mai mare sau egala cu 5")
#
# ############################
# # ex.9: Citeste o litera de la tastatura. Verifica daca e vocala
# litera = input("Introduceti o litera: ")
# vocale = 'aeiou'
# if litera.lower() in vocale:
#     print("Litera e Vocala")
# else:
#     print("Litera nu e vocala")
#  Verifica daca un numar x are exact 6 cifre
# x = float(input("Introdu o un sir de nr:"))
# # print(len(str(x)))
# import math
# x = str(x)
# if  x.count('.')>0 and len(x) == 7 or len(str(x)) == 6:
#     print("Are exact 6 cifre")
# else:
#      print("Peste minimum")

# INTALNIREA 03
#STRUCTURI DE DATE / COLECTII
# - Lista
# - Dictionar
# - Set
# - Tuple


######LIST:
# type([])
# Listele sunt niste variabile ce pastreaza mai mult de o valoare inauntrul lor
my_varr = 10
my_list = [1,2,3,4]
print(my_list)

my_list = [1, "doi", 3, True, 3, 3, 8.3, [100, 200, 300], (1,2,3), {'key': "val"}]
print (my_list)

my_list[0] # lista e indexata
print (my_list)

my_list[-1]
print (my_list)

my_list[1]
print (my_list)
# putem adauga noi valori la lista:
my_list.append(None)
print(my_list)
# => lista e mutabila fiindca se poate modifica fara suprascriere
print(my_list[-1])
s = 'abc' # cum fac sa ii adaug 'd' la final"? s sa devina 'abcd'
# s[-1] = 'd' # eroare
print(s)
# string ul trebuia suprascris
s = 'abc'
# s = s + 'd'
s += 'd'
print(s)
# outem adauga un elem nou si pe un anumit index
my_list.insert(2, 'avion')
print(my_list)
# putem scoate un element vechi
my_list.remove(8.3)
print(my_list)
my_list.remove(3) #atentie se sterge doar prima aparitie a elementului
print(my_list)
# putem sterge si de pe un index
del my_list[-1]
print(my_list)
[1, 2, 3] == [2, 1, 3] # e False
# => list e ordonata
# ce mai putem face cu listele?
print(my_list.count(3))
print(my_list)
print(type(my_list))
lst = [11, 3, 26, 1, 14, 13]
lst.index(1) #returneaza indexul respectiv
print(lst.index(1))
lst.sort(reverse=True)
print(lst)
lst = [5, 1, 2, 7, 4]
sorted_lst = sorted(lst)
print(sorted_lst)
print(lst)

#Proprietati lista:

lst = ['a', 'b', 'c']
# 1) lista e indexata
print(lst[0])
print(lst[-1])
# 2) lista e ordonata
l1 = [1,2,3]
l2 = [2,1,3]
print(l1 == l2) # False, conteaza ordinea!!!!
# 3)
lst = ['a', 'b', 'c']
lst.append('d') # adauga o noua val
lst[0] = 100 # sau chiar modific o val
print(lst)


###TUPLE
# tuplele sunt colectii similare cu listele, cu exceptia ca sunt imutabile
# odata create nu pot fi modificate!!!!!!!

my_tuple = (1, 'doi', 3, True, 3, 3, 7.4)
my_tuple = (1, 'doi', 3, True, 3, 3, 7.4, ('q', 'w')) # putem pune si [1,2,3], {'key: val'} dar nu recomandat
print(my_tuple [0])
print(my_tuple[-1])
(1,2,3) == (2,1,3) #=> False
# => tuple sunt ordonate
# my_tuple[0] = 100 # => EROARE!!!!! NU POATE FI MODIFICAT
print(my_tuple.index('doi')) #COUNT, ETC
# INSERT NU FUNCTIONEAZA

#PROPRIETATI TUPLA:
t = (12, True, 'abc', 0.8)

# tupla e indexata


# tupla e ordonata
t1 = (1,2,3)
t2 = (1,2,3)
t3 = (3,2,1)
print(t1 == t2)
print(t1 == t3)

# tupla e imutabila
# t[0] = 1000 # EROARE


# Avem tupla 1 = ('a', 10, 'b') si vrem sa adaugam valoarea 1234,
# obtinand tupla ('a', 10, 'b', 1234)?
t = ('a', 10, 'b')
t = list (t)
print(type(t))
t.append(1234)
t = tuple(t)
print(tuple(t))

# EXERCITIU PENTRU INTERVIURI
#DACA AVEM x = 5 si y = 10, cum facem sa le interschimbam valorile?
# Adica x = 10, iar y = 5?

x = 5
y = 10
aux = x
x = y
y = aux
print(f'x={x}, y={y}')

# Varianta smechera a Pythonul ui
x, y = y, x # se numeste tuple unpacking!
# practic (x, y) = (y, x) asa sa v-o imaginati
print(f'x={x}, y={y}')

# Tuple unpacking se foloseste frecvent la functii cand se returneaza mai mult decat o valoare
#
#
# DE LUAT NOTITELE!!!!!!!!!!!!!!!!


# DICTIONARELE
# Dictionarele sunt colectii / structuri de date care stocheaza elemente sub forma cheie:valoare

my_dict = {
    "brand": "Tesla",
    "model": "X",
    "year": 2022,
    "is_licensed": True,
    5: 10,
    2.1: "two point one",
    "avaiable_models": ['X', 'Y', 'S', '3'],
    "specs": {"top_speed": "250kmh", "range": "650km"},
    (1, 2, 3 ): 'o valoare'
}
# cheile din dict nu pot fi tipuri de date
# CHEILE DIN DICT TRB SA FIE TIPURI DE DATE IMUTABILE!!!!
# ATENTIE, nu putem avea o lista drept cheie in dict
# d = {[1,2,3]: 'valoare'} # EROARE


#LISTA e mutabila, python nu poate risca asta,
# in spate, in memorie valoarea e asociata cheii si e stocata
# intr o zona de memorie calculata pe baza acestei chei


## Codul urmator da sau nu eroare?

t = ('a', 'b', 'c')
d = {t: 'ahaa'}
print(d)

# accesam valorile prin intermediul cheilor
print(my_dict['brand'])
# nu prin indexi ca la str, list sau tuple
# print(my_pict[0]) #EROARE

# => DICT E NEINDEXAT

print(my_dict.keys()) #AFISEAZA CHEILE in ordinea in care au fost introduse

# => dict e ORDONAT!! (IN PY2 NU ERA)

# Putem adauga si alte elemente in dict precum:

my_dict['engine'] = 'electric'
print(my_dict)

#PUTEM MODIFICA
my_dict['model'] = 'S'
print(my_dict)

#PUTEM STERGE ELEM
del my_dict['year']
print(my_dict)

#PUTEM STERGE RETURNAND VALOAREA
val = my_dict.pop(5)
print(val)
print(my_dict)

#CUM RETURNAM RANGE-UL?

print(my_dict['specs']['range'])

# PROPRIETATI DICT:
my_d = {'brand': 'Tesla', 'model': 'S', 'year': 2022}
# dict e neindexat!!!!!!!
print(my_dict['brand'])
#print(my_dict[0]) ->> EROARE

# DICT E ORDONAT!!!!!!
# print(my_dict[''])

#DICT E MUTABIL

#CE FUNCTII MAI AU DICT-URILE?
d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}

print(d1.get('a'))
#echivalent cu
print(d1['a'])
# dar daca nu exista cheia returneaza un default
# print(d1['x']) #eroare
print(d1['a'])


# SET
# Seturile sunt colectii care stocheaza date imutabile si nu contine duplicate!!

my_set = {'alb', 'rosu', 22, False, (1,2,3), 2.66, 22}
print(my_set) #22 APARE O SINGURA DATA!!
# my_set[0] #EROARE SET NU ARE INDEX
# PUTEM ACCESA ELEM DOAR DACA ITERM PESTE SET
s1 = {'a', 'b', 'c'}
for elem in s1:
    print(elem)

# SAU PUTEM DACA DAM POP
print(s1.pop())
s1 = {'a', 'b', 'c'}
s1 = {'c', 'b', 'a'}

# s1 == s2 # E TRUE
#=> set e NEORDONAT

#PUTEM ADAUGA ELEMENTE NOI IN SET
s1.add ('zzzzz')
s1
#=> set e MUTABIL, DAR CONTINE D OAR ELEMENTE IMUTABILE!!!!

# PROPRIETATI SET:
s1 = {'alb', 'rosu', 'negru', 'albastru'}

s2 = {'negru', 'rosu', 'albastru', 'alb'}
print(s1 == s2) # e True

# set e mutabil
s1.add('verde')
print(s1)

# SETURILE SUNT ECHIVALENTUL PYTHON AL MULTIMILOR MATEMATICE

s1 = {'alb', 'rosu', 'negru', 'albastru'}
s2 = {'verde', 'alb', 'rosu', 'mov'}

#OPERATII CU SETURI:
#UNION - Elemente distincte
print('Union: ')
print(s1 | s2)

# INTERSECTION
print('Intersection: ')
print(s1 & s2)

# DIFFERENCE
print('Difference')
print( s1 - s2)

# SYMMETRIC DIFFERENCE
print('Symmetric difference: ')
print(s1 ^ s2 )


