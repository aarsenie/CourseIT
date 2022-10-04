#1. Avand lista
# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
####a. folositi for pt a itera prin toata lista si sa afisati:
                # 'Masina mea preferata este x'
####b. acelasi lucru cu un 'for each'
####c. acelasi lucru cu un while

# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
# #a.
# for elem in (masini):
#     print(f"Masina mea preferata este {elem}")

#b.
# for x in masini:
#     if x == 'Lastun':
#         continue
#     print(x)
#
# #c.
# import idx
# while masini:
#     for elem in masini:
#         print(f'Masina mea preferata este {masini}')
#     break
#2. Aceeasi lista
## folositi un for in for
    #Modificati elementele din lista astfel incat sa fie scrie cu majuscule, exceptand primul si ultimul (v1 - caracter, v2 - element)
# Printati varianta finala a listei
# Incercati sa rezolvati atat v1 => output: ['aUDi', 'vOLVo', 'bMw', 'mERCEDEs', 'aSTON MARTIn', 'lASTUn', 'fIAt', 'tRABANt', 'oPEl']
# Cat si v2 => output: ['audi', 'VOLVO', 'BMW', 'MERCEDES', 'ASTON MARTIN', 'LASTUN', 'FIAT', 'TRABANT', 'opel']

# masini = ['Audi', 'Volvo', 'BMW' , 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
# for i in range (0, len(masini)):
#     masini[i] = (masini[i][0].lower()+masini[i][1:-1].upper()+masini[i][-1].lower())
# print(masini)

# print(masini.index("Opel"))
# print(masini.index("Audi"))

masini = ['Audi', 'Volvo', 'BMW' , 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
for i in range(len(masini)):
    if i == 0 or i == len(masini)-1:
        masini[i] = masini[i].lower()
    else:
        masini[i] = masini[i].upper()
print(masini)


# for i in range (0, len(masini), -1):
#     if i != 0 and i !=len(masini)-1:
#         masini[i] = ([masini[i][:0:].lower()] + [masini[i][1:-1].upper()] + [masini[i][:-1:].lower()])
# print(masini)
#
# for index, masina in enumerate(masini):
#     print(index, masina)
# lista = []
# lista.append('element1')
# lista.append('element2')
# print(lista)
# for masina in masini:
#     print(lista[0].lower())
# masini = ['Audi', 'Volvo', 'BMW' , 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
# v1 = []
# for marca in masini:
#     v1.append(marca.upper())
# print(v1)
# for i in masini:
#     i[0] = [i[0].lower() + i[-1] for i in v1]
# print(v1)
#3. Aceeasi lista
#Vine un cumparator care doreste sa cumpere un Mercedes
# Iterati prin ea prin for each
# Daca masina e mercedes (if)
#    Printam ‘am gasit masina dorita de dvs’
#    Iesim din ciclu folosind un cuvant cheie care face acest lucru
# Altfel:
#    Printam Am gasit masina X. Mai cautam
#

# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
#
# for marca in masini:
#     if marca =='Mercedes':
#         print('Am gasit masina dorita de dvs')
#         break
#     else:
#         print(f'Am gasit masina {marca}. Mai cautam.')

# 4.
# Aceasi lista
# Vine un cumparator bogat dar indecis. Ii vom prezenta toate masinile cu exceptia Trabant si Lastun.
# Daca masina e Trabant sau Lastun
#    Folositi un cuvant cheie care sa dea skip la ce urmeaza
# Printati S-ar putea sa va placa masina x

# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
#
# for marca in masini:
#     if marca == 'Trabant':
#         continue
#     elif marca == 'Lastun':
#         continue
#     else:
#         print(f'S-ar putea sa va placa {marca}!')

#5. Modernizati parcul de masini
# Creati o lista goala, masini_vechi
# Iterati prin masini
# Cand gasiti Lastun sau Trabant:
# Salvati aceste masini in masini_vechi
# Suprascrieti-le cu ‘Tesla’ (in lista initiala de masini)
# Printati Modele vechi: x
# Modele noi: x

#
# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
# masini_vechi = []
# for marca in masini:
#     if marca =='Lastun':
#         masini.remove('Lastun')
#         masini_vechi.append('Lastun')
#         masini.insert(7,'Tesla')
#     elif marca =='Trabant':
#         masini.remove('Trabant')
#         masini_vechi.append('Trabant')
#         print(masini)
#         print(masini_vechi)
#
#
# # 6.
# Avand dict
# pret_masini = {
#     'Dacia': 6800,
#     'Lastun': 500,
#     'Opel': 1100,
#     'Audi': 19000,
#     'BMW': 23000
# }
# Vine un client cu un buget de 15000 euro
# Prezentati doar masinile care se incadreaza in acest buget
# Iterati prin dict.items() si accesati masina si pretul
# Printati Pentru un buget de sub 15000 euro puteti alege masina x
# Iterati prin lista


pret_masini = {
    'Dacia': 6800,
    'Lastun': 500,
    'Opel': 1100,
    'Audi': 19000,
    'BMW': 23000
}
for item in pret_masini.items():
     if item[1] <= 1500:
         print(f"Pentru un buget de sub 15000 EURO puteti alege masina", item[0], "cu pretul de", item[1], "ron")

#7. Avand lista
# numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# Iterati prin ea
# Afisati de cate ori apare 3
# (nu aveti voie sa folositi count)

from collections import Counter
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
counts = Counter(numere)
print(counts[3])

#8.
# Aceeasi lista
# Iterati prin ea
# Calculati si afisati suma numerelor
# (nu aveti voie sa folositi sum)
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
count = 0
total = 0
for n in numere:
    total += n
print(total)

#9.
#Aceeasi lista
# Iterati prin ea
# Afisati cel mai mare numar
# (nu aveti voie sa folositi max)
#
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
length = len(numere)-1
for n in range(length):
    if numere[n] > numere[n + 1]:
        numere[n], numere[n + 1] = numere[n + 1], numere[n]
print(numere[-1])

#10.
#Aceeasi lista
# Iterati prin ea
# Daca numarul e pozitiv, inlocuiti-l cu valoarea lui negativa
# Ex: daca e 3, sa devina -3
# Afisati noua lista
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
numere_opuse = [ -x for x in numere ]
length = len(numere)
for n in range(length):
    if n == 0:
        print(numere_opuse)

########
# #11.
# alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
# numere_pare = []
# numere_impare = []
# numere_pozitive = []
# numere_negative = []
# Iterati prin lista alte_numere
# Populati corect celelalte liste
# Afisati cele 4 liste la final
alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
numere_pare = []
numere_impare = []
numere_pozitive = []
numere_negative = []
for i in alte_numere:
    if i % 2 == 0:
        numere_pare.append(i)
    elif i % 2 == 1:
        numere_impare.append(i)
for i in alte_numere:
    if i > 0:
        numere_pozitive.append(i)
    elif i < 0:
        numere_negative.append(i)
    else:
        print("Niciunul")
print("Numere Pare:", numere_pare)
print("Numere Impare:", numere_impare)
print("Numere Pozitive:", numere_pozitive)
print("Numere Negative:", numere_negative)

###### 12.
rows = 7
# outer loop
for i in range (rows+1):
    # nested loop
    for j in range (i):
        #display number
        print(i, end='')
    #new line after each row
    print('')

##########



