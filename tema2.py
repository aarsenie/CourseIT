# # 1. Explica cum functioneaza un if else
# # Functia if else este o conditionare a unei operatii pe care vrem sa o efectuam.
# # Pentru outcome ul dorit, vom determina variabilele si conditiile necesare.
#
# # 2. Verifica si afiseaza daca x este numar natural sau nu
#
# x = float(input("Introdu un numar:"))
# if x >= 0:
#     print ("Numar natural")
# else:
#     print("Numar nenatural")
# # print(len(x) == 1 and x.isdigit() and x> '0')
# # ##
# # x = '1'
# # print(len(x)) == 1 and '1' <= x <= '9'
# # ##
# # int(x) > 0
# # print (0 < int(x) <= 9)
# ##
#
# # 3. Verifica si afiseaza daca x == numar pozitiv, negativ sau neutru
# x = float(input("Introdu un numar:"))
# if x > 0:
#     print("Numar Pozitiv")
# elif x == 0:
#     print("Numar Neutru")
# else:
#     print("Numar negativ")
#
# # 4. Verifica si afiseaza daca x este intre -2 si 13
#
# x = float(input("Introdu un numar:"))
# if x in range (-2, 13):
#     print ("Adevarat")
# else:
#     print("Fals")
#
# # 5. Verifica si afiseaza daca diferenta intre x si y este mai mica de 5
#
# x = float(input("Introdu un numar:"))
# y = float(input("Introdu un al doilea numar:"))
# [x[y+5]-x[y] for y in range(-5)]
# if x < y:
#     diff = y - x
# else:
#     diff = x - y
#     print('Diferenta intre x si y =', diff)
#

# # 6. Verifica daca x NU este intre 5 si 27. (functia NOT)
#
# x = float(input("Introdu un numar:"))
# if x not in (5, 27):
#     print("x nu se afla intre 5 si 27")
# else:
#     print("x se afla intre 5 si 27")
#
# # 7. x & y (int) -
# #    Verifica si afiseaza daca sunt egale,
# #   daca nu afiseaza care dintre ele este mai mare
# x = float(input("Introdu un numar:"))
# y = float(input("Introdu un numar:"))
# if x == y:
#     print("Sunt egale")
# else:
#     print("Nu sunt egale")

########################
# x = int(input("introduceti x:"))
# y = int(input("introduceti y:"))
#
# if (x-y)==0:
#     print("cele doua numere sunt egale")
# elif(x-y)<0:
#
#     print("numarul y este mai mare")
# else:
#     print("numarul x este mai mare")
##########################
# # 8. x, y,z - laturile unui triunghi
# # Afiseaza daca triunghiul este isoscel, echilateral sau oarecare
#
####################
#print("Input laturile unui triunghi")
# x = float(input("Introdu un numar:"))
# y = float(input("Introdu un numar:"))
# z = float(input("Introdu un numar:"))
# if x == y == z:
#     print("Triunghi echilateral")
# elif x==y or y==z or z==x:
#     print("Triunghi isoscel")
# else:
#     print("Triunghi oarecare")
######################################
# x = float(input("latura x:"))
# y = float(input("latura y:"))
# z = float(input("latura z:"))
# if x<y+z and y<x+z and z<x+y:
#     print("x, y, z sunt laturile unui triunghi")
# else:
#     print("x, y, z nu sunt laturile unui triunhi")
# if x == y == z:
#     print("Triunghi echilateral")
# elif x==y or y==z or z==x:
#     print("Triunghi isoscel")
# else:
#     print("Triunghi oarecare")

# # 9. Citeste o litera de la tastatura
# #    Verifica si afiseaza daca este vocala sau nu
# x = input("Introdu o litera:")
# if x in ('a','e','i','o','u'):
#     print("Litera este o vocala")
# else:
#     print("Litera este o consoana")
#
# # 10. Transforma si printeaza notele din sistemul romanesc in >
# # 9=> A; 8=> B; 7=> C; 6=> D; 4 => E; -4 => F
# print(f'Notele din sistemul romanesc')
# x = float(input("Introdu o nota:"))
# if x == 9:
#     print('A')
# if x == 8:
#     print('B')
# if x == 7:
#     print('C')
# if x == 6:
#     print('D')
# if x == 4:
#     print('E')
# elif x < 4:
#     print('F')

# 11. Verifica daca x are MINIM 4 cifre (x e int)
# (ex: 1234 are 4 cifre, 10 nu are minim 4 cifre)

# x = float(input("Introdu o un sir de nr:"))
# import math
# bool_adv = 4 <math.inf
# bool_fals = 4 <-math.inf
# if x <= math.inf:
#     print("Minimum 4 cifre")
# else:
#     print("Peste minimum")
#12. Verifica dasca x are exact 6 cifre
# x = float(input("Introdu o un sir de nr:"))
# import math
# bool_adv = 6 <math.inf
# bool_fals = 6 <-math.inf
# if  x <= math.inf:
#     print("Are exact 6 cifre")
# else:
#      print("Peste minimum")
# nu este corect
#13. Verifica daca x este numar par sau impar (x e int)
# x = int(input("Introdu o un numar:"))
# if x / 2:
#     print("Numar par")
# else:
#     print("Numar impar")
# ####################
# x = int(input("Introdu o un numar:"))
# r = x%2
# if r==0:
#     print("x este numar par")
# else:
#     print("x este numar impar")
# #####################
# 14. x, y, z (int)
# Afiseaza care este cel mai mare dintre ele?
# x = int(input("Introdu o un numar pentru x:"))
# y = int(input("Introdu o un numar pentru y:"))
# z = int(input("Introdu o un numar pentru z:"))
#
# if x > y and x > z:
#     print("x cel mai mare")
# elif y > x and y > z:
#     print("y cel mai mare")
# elif z > x and z > y:
#     print("z cel mai mare")
#
# 15. x, y, z - reprezinta unghiurile unui triunghi
# Verifica si afiseaza daca triunghiul este valid sau nu

# x = float(input('Introdu unghiul pentru x:'))
# y = float(input('Introdu unghiul pentru y:'))
# z = float(input('Introdu unghiul pentru z:'))
#
# if x+y>=z and y+z>=x and z+x>=y:
#         print("Triunghi valid")
# else:
#         print("Triunghi invalid")
# 16. Avand stringul: 'Coral is either the stupidest animal or the smartest rock'
# cititi de la tastatura un int x
# afiseaza stringul fara ultimele x caractere
# ex: daca ati ales 7 => 'Coral is either the stupidest animal or the smarte'

# s1 = 'Coral is either the stupidest animal or the smartest rock'
# count = 0
# for i in s1:
#     count = count - 6
# s2 = s1 [0:-6] + s1 [count - 6:count]
# print("s1 = " +s2)
# 17. Acelasi string
#     Declara un string nou care sa fie format din
#     primele 5 caractere + ultimele 5

# s1 = 'Coral is either the stupidest animal or the smartest rock'
# count = 0
# for i in s1:
#     count = count + 5 and - 5
# s2 = s1 [0:5] + s1 [count - 5:count]
# print("s1 = "+s2)

# 18. Acelasi string
# salveaza intr-o variabila si afiseaza indexul de start al cuvantului rock
# (hint: este o functie care te ajuta sa faci asta)
# folosind aceasta variabila + slicing, afiseaza tot stringul pana la acest cuvant
# output: 'Coral is either the stupidest animal or the smartest '

# s1 = 'Coral is either the stupidest animal or the smartest rock'
# print(s1.rfind("rock"))
# count = 0
# for i in s1:
#     count = count - 5
# s2 = s1 [0:-5] + s1 [count - 5:count]
# print("s1 = " + s2)

# TO DO #EX_02: Given a string s1, append another string s2 in the middle of s1
# e.g.: s1 = 'Legendary, s2 = 'wait' => 'Legewaitndary'
#       s1 = 'mama', s2 = 'MIA' => 'maMIAma'

# str1= 'koko'
# print(str1)
# str1 = str1[:2]  + "Roco" + str1[2:]
# print(str1)


# EX_03: Given a keyboard inputed number: print "Your  number is pozitive" or "Your number is negative"or "Your number is 0"
# depending wether the number is greater than 0, smaller or 0.
# nr = int(input("Introdu un numar:"))
# if nr > 0:
#     print("Your number is pozitive")
# elif nr < 0:
#     print("Your number is negative")
# else:
#     print("Your number is 0")
#
x = int(input('Ghiceste un numar:'))
import random
y = random.randint(1,6)
print(y)
if x < y:
    print(f'Ai pierdut. Ai ales un numar mai mic. Ai ales {x}, dar a fost {y}.')
elif x > y:
    print(f'Ai pierdut. Ai ales un numar mai mare. Ai ales {x}, dar a fost {y}.')
else:
    print(f'Ai ghicit. Felicitari! Ai ales {x} si zarul a fost {y}.')

