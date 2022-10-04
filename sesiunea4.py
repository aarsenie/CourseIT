# # #CICLURI REPETITE.LOOP:
# # #while
# # # WHILE e o bucla (LOOP) care face iteratii, o bucla cu nr necunoscut de iteratii (repetari)
# # # in care blocul de cod se EXECUTA atata timp cat CONDITIE E ADEV
# #
# # # i = 1
# # # while 1 <= 3: # CONDITIA TREBUIE la un mom dat sa nu mai fie adev
# # #     print(i)
# #     # i+=1 # sa nu uitati incrementarea, altfel intrati in CICLU INFINIT
# #
# #
# # # SINTAXA WHILE
# # # while conditie_adevarata:
# #         #se executa blocul de instructiuni
# # # ne putem imagina ca vrem sa mergem pe stadion la alergat
# # # ne propunem sa alergem atata timp cat putem
# # # exista si bloc else (ca la if) exe o singura data in mom in care while dev falsa
# # mai_pot_o_tura = True
# # while mai_pot_o_tura:
# #     print("Am mai alergat o tura!")
# #     mai_pot_o_tura = bool(int(input("Mai poti o tura? introdu 1 pt da, 0 pt nu:")))
# # else:
# #     print("Am terminat de alergat!")
# # print("Acum pot servi desert")
# # # bool("")) #FALSE
# # # bool("qweqwe") #orice alt string e True
# #
# #
# # # vrem sa dam cu zarul
# # # sa ne oprim cand apare un 3 sau 6
# # import random
# # dice_roll = 0
# # # while dice_roll != 3 and dice_roll != 6:
# # while dice_roll not in (3,6):
# #     dice_roll = random.randint(1,6)
# #     print(f"Dice rolled: {dice_roll}")
# import idx as idx
#
# # FOR
#
# # for - e o bucla cu nr cunoscut de iteratii (pasi/repetari) in care se itereaza
# # peste o secventa si se exdecuta un bloc de cod in mod repetat
# # pt cate elemente sunt in secventa respectiva
#
# # secventa = lista, tupla, set, dict, string, range(), ....
#
# # SINTAXA FOR
# # for element in secventa:
# #     #bloc de instructiuni
# #     # (faem ceva cu element)
# # ne imaginam ca mergem pe stadion la alergat
# # ne propunem sa alergam 5 ture
# for tura in range(5):
#     print("Am mai alergat o tura! tura nr: {tura}")
# for elem in [1,2,3]:
#     print(elem)
# for elem in (1,2,3):
#     print(elem)
# for elem in "abc":
#     print(elem)
#
# #ATENTIE NU ITERATI PESTE NUMERE!!!!!!!
# # for elem in 1000: EROARE
#
# country = {'name': 'Romania', 'population': '19.5mil', 'Continent': 'Europe'}
# # ca sa retur val de la cheia name
# # key = 'name'
# print(country['name'])
#
# for key in country:
#     print(country[key])
# for key, val in country.items():
#     print(f"key={key}, value={val}")
# countries = ['Romania','USA','UK','Italy']
# #vrem sa afisam elem cat si indexul pe care se afla
# for elem in enumerate(countries):
#     print(f"Elementul {elem} se gaseste pe indexul {idx}")
#
# # exista si bloc else, exe o singura data in mom in care am terminat de iterat
# for c in countries:
#     print(f"You're visiting {c}")
# else:
#     print(f"Vacation is done, back to work!")

# C4_EX01: Print all even natural numbers lower than a keyboard inputed one.
#e.g: input = 9 => 0 2 4 6 8
# x = int(input("Introdu un numar: "))
# for x in range(0, x):
#     if (x % 2 == 0 ):
#         print(x)

# CA_EX01: Given a nr n=15, write a loop
# that prints the number and decreases it
#until it hits 0 by:
# - 2 in case the number is divisible by 5
# - 3 if it is even;
# - 1 if it is odd.
n = 15
# n => 13; n => 12; n => 9; n=> 8; n=> 5;...
# while n > 0:
#     print(n)
#     if (n % 5 == 0):
#         n -= 2
#     elif(n % 2 == 0):
#         n -= 3
#     else:
#         n -= 1
#

# BREAK
# Break - opreste iteratia, iesind din bucla;
# executia va continua cu instructiunile de dupa bucla

import random
dice_roll = 0
while True: # conditia, in teorie, e mereu adevarata
    dice_roll = random.randint(1,6)
    print(f"Dice rolled: {dice_roll}")
    if dice_roll in (3,6):
        break
    else:
        print("While ended") #Atentie, daca iesim din bucla cu break,
                            # else nu se mai executa!
    print("After break, execution continues here...")

for nr in range (9):
    if nr == 10:
        break
    print(nr)
else:
    print("For finished...") #Atentie, printul se mai afis daca iesim din break inainte
print("After break execution continues here...")

# CONTINUE
# Intrerupe iteratia curenta si sare la iteratia urmatoare
# CONTINUE == SKIP

# nr = 5
# while nr > 0:
#     nr -= 1
#     if nr == 2:
#         continue
#     print(nr) # cand nr e 2, nu mai ajunge sa-l printeze,
#                 # ci continua cu urm iteratie
for nr in range(9):
    if nr % 2 ==0:
        continue
        print(nr)



# PASS
# PASS nu afecteaza codul in niciun fel, singura utilitate:
                #ci tine loc de comanda pentru a nu primi eroare

print("Inainte de for")
for nr in range (10): # presupunem ca dintr un oarecare motiv vrem sa iteram,
                    # dar nu vrem sa facem nimic inauntrul for ului
# PASS tine loc de comanda sa nu primim IndentationError
    pass
print("Dupa for")

