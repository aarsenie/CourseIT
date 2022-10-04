# 1. In cadrul unui comm explica ce inseamna o variabila.
# => O variabila este o zona din memorie ce retine date.
# 2. Declara si Initializeaza cate o variabila din:

#STRING
locatie = 'Venetia'
#INT
declarat = 1979
#FLOAT
suprafata = 415.9
#BOOL
capitala_provincie = True

# 3. Utilizeaz functia "TYPE"

my_ap = "11a"
print(type(my_ap))

# 4. Rotunjeste "float-ul" cu functia round()
#    Salveaza aceeasi modificare
#    in aceeasi variabila (suprascriere)
#    Verifica tipul acesteia

print(round(suprafata))
suprafata = 416
print(type(suprafata))

# 5. Fol. "print" in consola si
# print 4 propozitii  folosind cele 4 variabile.
import selenium.webdriver.common.devtools.v85.profiler

numeElev = 'Alexandra'
varsta = 21
studenta = False
medieBac = 8,20

print(f'Numele elevei este {numeElev}')
print(f'Are varsta {21}')
print(f'Studii in prezent {studenta}')
print(f'Cu media de bac {medieBac}')

# 6. citeste din tastatura - input - nume, prenume
# afiseaza ' numele complet are x caractere'

nume = input('Introdu nume: ')
prenume = input('Introdu prenume: ')

print(f'Numele complet are {len(nume + prenume)} caractere')

# 7. citeste din tastatura - lungimea - latimea
# afiseaza 'aria dreptunghiului este x'

lungimea = 8
latimea = 4
aria = lungimea * latimea
print(f'Aria dreptunghiului este {aria}')

# 8 & 9. string 'Coral is either the stupidest animal or the smartesc rock'
# afiseaza de cate ori apare "the"

text = 'Coral is either the stupidest animal or the smartest rock'
print(text.count(' the '))
occurences_the = text.count(' the ')
print(f"Cuvantul the apare de {occurences_the} ori")

# 10.

text = 'Coral is either the stupidest animal or the smartest rock'





