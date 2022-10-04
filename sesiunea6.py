# RECAPITULARE
# def discount(pret, reducere=10): #putem definii unul dintre parametrii direct!!!
#     if reducere > 0 and reducere <100:
#         pret = pret - (reducere/100 * pret)
#         print(pret)
#     else:
#         print('Ati aplicat o reducere invalida')
# discount(100,10)

 # Recap01: What do we mean by data type? give ex of numeric data type in python

 # data type = reprezinta ce tip de date are o variabila

a = 123 # int
b = 1.1 # float

# str - nu e numeric

# Recap02: What vis the data type
# and possible values for repr. a truth conditiom?
# How about missing value?

# truth condition: bool, aka boolean
# possible values: True/False

# missing value: NoneType, with value of: None
# type(None)

# Recap03: What is variable? Give us an example!
# variable = e o forma/caseta de stocheaza date; are un nume si o val si ma iare un loc in memmorie unde salvata
my_string = "Oana"
lst = [1,2,3]

#Recap04: What naming convention would we use if we want to take a variable called: my first variable; having value 10?

my_first_variable = 10

# Recap05: What's the name of the built-in function which returns the data type of a given value/variable?
# What will it return for calling it with the value "120.0"?

# type
type("120.0") #str

# Recap06: What would the following piece of code print?

n = 11
print(n/3)
print(n//3)

# Recap07: What would the following piece of code print?

my_text = 'yes'
print(my_text + ' of course ')

# Recap08: What would the following piece of code print?
my_text = 'yes'
print(my_text + '3') #eroare fara ghilimele

# Recap09: What would the following piece of code print?
my_text = 'yes'
print(my_text * 3)
lst = [12, 13] * 10
print(len(lst))
print(lst)
# Recap10: How should we write the print statement to retrive the truth value from the comparison of a integer a=8
# being bigger than both b=6 and c=3

a = 8
b = 6
c = 7
if a > b and a > c:
    print(True)
else:
    print(False)

print(a > b and a > c)

# Recap11: How should we write the print statement to retrieve the truth value of wether a string s1='str'
# is contained in a string s2='substring'?

s1 = 'str'
s2 = 'substring'

print(s1 in s2)

# Recap12: How should we write the print statemtent to retrieve pi two zecimals

pi = 1.13159
print(str(pi)[0:4])
print(round(pi, 2))
print(f"{pi:.2f}")

# Recap13: What is the true value of the following code?

a = True
b = True
c = False
print(not a or b and c)
#     False or True and False
#           True    and False
#                   False

# Recap14: Given the string hello = "Hello, World!", what should we write to get the string formed of the first 5 characters?
# aka "Hello"?

hello = "Hello, World!"
print(hello[0:5])

# Recap15: Given the string hello = "Hello, World!", what should we write to get the 2 words
# separated in a list like this ["Hello", "World"]?

hello = "Hello, World!"
hello = hello.strip('!')
print(hello.split(', '))

# Recap16: Given the string hello = "Hello, World!", what shoukld we write
# to get the substring "eoWL"?

hello = "Hello, World!"
#       0123456789....
print(hello[1::3]) # ne int 1,4,7,10 slice[start:stop:step]
print(hello[::-1])


# OOP ---------------

# oop = Object oriented programming
car = 'Dacia' # obiectul car care e de tipul/clasa string

# clasa - e o schita/sablon pt a crea obiecte.entitati,
# definind atribute (caracteristici) si metode (functionalitati)

class Car:
    #### ATTRIBUTE / FIELDS
    brand = 'Dacia'
    model = '1310'
    year = 1970

    #### METHODE
    def accelerate(self):
        print("VRUUUUUMMM")

    def show_year(self):
        print(self.year)
    def add_sears(self, nr_of_seats):
        self.seats = nr_of_seats

my_car = Car()
my_car.accelerate()
my_car.show_year()
print(my_car.brand)


dacia = Car()
print(dacia.model)

class Car:
    #constructor
    def __init__(self, input_brand, input_model, input_year, input_has_leather=True ):
        self.brand = input_brand
        self.model = input_model
        self.year = input_year
        self.has_leather = input_has_leather

    def add_seats(self, nr_ofseats): #CAZSPECIAL - vedem daca putem adauga atribute in afara innit,
                            # dar de obicei, atributele se trec in init
        self.seats = nr_ofseats

tesla = Car('Tesla', 'Y', 2022)
print(tesla.brand)
print(tesla.year)
print(tesla.has_leather)

vw = Car('VW', 'Passat', 2020)
print(vw.brand)

audi = Car('Audi', 'A7', 2022) # am initializat un obiect numit audi din clasa Car
audi.add_seats(5)
print(audi.seats)

# del audi.seats #merge, dar nu e uzual..
# print(audi.seats)




# sa presupunem ca avem un fisier numit oop1.py unde avem doar def clasei
# si mai avem un fisier oop2.py in care instantiem si ne jucam cu niste obiecte ale clasei
# ca sa putem folosi oop2.py clasa respectiva, trb sa o importam in interiorul oop2.py cu:

# from oop1 import NumeClasa
# doar daca ambele fisiere sunt in acelasi director!!!!!!!!
# MyProject
# - oop1.py
# - oop2.py
# putem importa clase/functii din alte fisiere cu:

# from director.fisier import NumeClasa
# sau
# from director.fisier import nume_functie

# fisierele cu extensia .py se numesc module python
# iar folderele/directoarele care contn un fisier __init__.py -> se numesc package-uri

# import math
# print(math.sqrt(16))
# from director1.fisier import NumeClasa obj = NumeClasa()
# from director1.fisier import NumeClasa as NC # si folosim clasa cu noul alias: obj = NC()
# from director1 import fisier # si folosim obj = fisier.NumeClasa1() sau obj = fisier.NumeClasa2()
# from director1 import fisier as the_file # si folosim the_file.NumeClasa1()......
# import math
# import datetime
# # sau putem import librarii externe (daca le avem instalate)
# import
# from __main__ import Car as Masina
# my_car = Masina("Audi", "Q5", 2013)
# my_car.accelerate()