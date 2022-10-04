# user = input('Insert your user: ')
# password = input("Insert your password: ")
# password_mask = len(password) * "*" #numarul de caractere in stelute nr_char * "*"
#
# print (f'Parola pentru user {user} este {password_mask} isi are {len(password)} caractere')
# pi = 3.146583
# print(f'Valoarea lui pi cu doua zecimale este: {round(pi, 2)}')
# print(f'Valoarea lui pi cu doua zecimale este: {round(pi:2f)}')
# "{}".format'('o valoare')

# Daca era strig pi?
# pi = "3.145783"
# pi = str(pi)
# print(f"Valoarea lui pi cu doua zecimale este: {pi[0:4]}")

# OPERATORI & CONDITIONALI IF ELSE ELIF

# += - X +=3 - X = X + 3
# -= {....}
# *= {...}
# /=  x/= 3

# OPERATORI DE ATRIBUIRE =, +=, -=, *=, /=

# Avem x = 10 si vrem sa il marim de 5 ori
x = 10
# x = x * 5 #DONT!!!
x *= 5
print(x)



y = 12
# vrem sa il injumatatim pe y
y /= 2
print (y)

#OPERATORI ARITMETICI

x = 2
y = 5
print (x + y)
print (x * y)
print (y / x)

x = 11
y = 3
print (x / y) # impartire cu zecimale
print ( x % y) # impartire cu rest
print ( x // y) # returneaza partea intreaga (catul)

# D / I = C + R
# // returneaza C
# % returneaza restul
x = 11
y = 3
print (x % y)
# 11 / 3 = 3 r 2

x, y, z = 2, 4, 8
print (z / y / x) # se pastreaza ordinea efectuarii operatiilor de la mate!!

x = 10
# print (x / 0) # EROARE IN PYTHON BY DIVISION WITH ZERO

print (1 + 2 + 5 * 2 - 2)
print (1 + (2 + 5) * 2 - 2)

# presupunem ca x = 22; vrem sa determinam x e par sau nu?

x = 22
x % 2 == 0
print (x % 2)

x = 3
x ** 3
# 3 ^ 3 = 3 * 3 * 3 = 27

x = 2
pow(x, 3)
# pow=exponential

# OPERATORI DE COMPARARE ==(EQUAL), !=(NOT EQUAL), >, <, >=, <=
print (5 > 2)
print (5 < 2)
print (5 == 2)
print (5 != 2)

s1 = 'abc'
s2 = 'bcd'
print ( s1 > s2)
print ( s1 < s2) # comparatie se face pozitie cu pozitie

s1 = 'abc'
s2 = 'xy'
print (s1 < s2)

#ord('a')
#ord('x')

print (5 != 5)

# OPERATORI LOGICI and, or, not

# and = returns true if statements are true

# A | B | and | or | not A
True and False #=> FALSE
# True | True | TRUE | TRUE | False
# True | False | FALSE | TRUE | False
# False | True | FALSE | TRUE | True
# False | False | TRUE | FALSE | True

False or not False and True
# False or True and True
# True and True
# True
False and False or True and True
# False or True and True
# True and True
# True
print (False and (False or True) and True)
# False and True and True
# False and True
# False
print (not(5 > 7))
# True
x = 12
x < 7 or x > 10
x = 10
y = 8
z = 11
# vrem sa verificam daca x > decat y si mai mare decat z
print((x > y) and (x > z))

# OPERATORI DE IDENTITATE = IS & IS NOT

a = 2
b = 2
c = a
print ( a is b) # verifica daca sunt stocate in acelasi loc
print ( a is c)
print ( b is c)

s1 = 'qwe'
s2 = 'qwe'
s3 = s1
print (s1 is s2)
print (s2 is s3)
print (s3 is s1)

# 11 = [1,2,3]
# 12 = [1,2,3]
# 13 = 11
# print (11 is 12)
# print (12 is 13)
# print (13 is 11)

a = 2
b = 2
c = a
print (id(a))
print (id(b))
print (id(c))

# OPERATORI DE MEMBRU = IN & NOT IN (a list)

print('a' in 'apple')
print ('pp' in 'apple')
print ('ppp' in 'apple')

#2 in [1,2,3] = false
# '2' in '12' = true
# "fox" in "dog, cat, foxy, horse" = true


# EX_01: Create a substring made of the first, middle and last character of a given string
# e.g.: 'Michael' => 'Mhl'
#       'Adrian' => 'Arn' / 'Ain' (either one works)
s1 = 'Alexandra'
# print(len(s1))
# print(len(s1)/2)
# first_char =s1[0]
# middle_char = s1[int(len(s1) / 2):int(len(s1) / 2)]
# last_char = s1[int(len(s1) - 1):int(len(s1) - 1)]
# res = first_char + middle_char + last_char
# print(res)

count = 0
# loop through the string
for i in s1:
    count = count + 1
s2 = s1 [ 0:2] + s1 [count - 2: count]
# printing the new string
print("s1 = " + s2)
print("s2 = "+ s2)

#OR:
# s = input("Introdu un string: ")
# primaLitera = s[0]
# index_jumatate = len(s) // 2
# litera_jumatate = s[index_jumatate]
# ultimaLitera = s[-1]
# substring = primaLitera + litera_jumatate + ultimaLitera
# print(substring)

# TO DO #EX_02: Given a string s1, append another string s2 in the middle of s1
# e.g.: s1 = 'Legendary, s2 = 'wait' => 'Legewaitndary'
#       s1 = 'mama', s2 = 'MIA' => 'maMIAma'

# IF - FLOW CONTROL

A = 5
B = 4
if A > B:
    print("Da, A e mai mare decat B")

A = 5
B = 10
if A > B:
    print("Da, A e mai mare decat B")
print ('Asta se afiseaza?') # ATENTIE LA INDENTARE!!

#Cum facem sa afisam mesajul "Ai picat examenul, ne vedem la vara."
# in cazul in care nu e de trecere?
nota_de_trecere = 4.5
nota = float(input('Alege nota: '))
if nota > nota_de_trecere:
    print(f'Felicitari, ai trecut examenul cu nota {nota}')
else:
    print("Ai picat examenul, ne vedem la vara.")

# Robot telefonic cu mai multe optiuni
# 1 = romana; 2 = engleza, 0 = meniu anterior, altceva => Optiune Invalida
# optiuni = input("Alegeti o limba: ")
# if optiune == '1':
#     print('Ati ales limba romana')
# elif optiune == '2':
#     print('Ati ales limba engleza')
# elif optiune == '0':
#     print('Ati ales meniul anterior')
# else:
#     print('Optiune Invalida')

# sintaxa if
# if cond:
       # ramura se executa daca cand e adevarata
# elif alta_cond:
       # ramura se executa daca cand e falsa, dar alta_cont e adev
# else:
       # ramura care se executa cand niciuna dintre conditiile anterioare nu e adev

# elif si else nu trebuie neaparat sa apara

# EX_03: Given a keyboard inputed number: print "Your  number is pozitive" or "Your number is negative"or "Your number is 0"
# depending wether the number is greater than 0, smaller or 0.








