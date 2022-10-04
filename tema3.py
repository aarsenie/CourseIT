#1. Declara o lista note_muzicale. {do, re, mi, fa, so, la, si, do}
# Afiseaz o; Inverseaza ordinea (SLICING) & suprascrie lista.
# Printeaza varianta actuala (INVERSATA)
# Aplica o metoda care banuiesti ca face acelasi lucru(metoda de inversare)
                                # NU TREBUIE SUPRASCRISA (se face automat)
# Printeaza varianta actuala. Practic ajuns la varianta initiala.

#######SLICING e temporar. Pentru noua varianta se va face suprascriere
                            # sau salvare intr o alta lista
        # Metoda gasita face suprascrierea automat. Modificari permanente.
        # Ambele variante sunt utile.




note_muzicale = ["do", "re","mi", "fa", "sol", "la", "si", "do"]
print(note_muzicale)
print(note_muzicale[: :-1]) #SLICING
note_muzicale = ['do','si','la','sol','fa','mi','re','do'] #SUPRASCRIERE
print(note_muzicale)
print(list(reversed(note_muzicale))) #reversed returneaza tipul list
print(note_muzicale[::-1])
#Revenit la varianta initiala.



# 2. De cate ori apare 'do'?
print(note_muzicale.count('do'))

#3. Cu cele doua liste [3, 1, 0, 2] & [6, 5, 4]
    #gaseste doua variante sa le unesti intr-o singura lista.

my_list1 = [3, 1, 0, 2]
my_list2 = [6, 5, 4]
my_list = my_list1 + my_list2
print(my_list)

#4. # Sorteaza si afiseaza lista generata la ex anterior
    # sorteaza numarul 0 folosind o functie #?
    # afiseaza iar lista

my_list = sorted(my_list)
print(my_list[0])
print(my_list)

#5. Folosind un if verifica lsita generata la ex 3 si afiseaza:
    # lista este goala.
    # lista nu este goala
if not my_list:
    print("Lista este goala.")
else:
    print("Lista nu este goala")

# 6. Foloseste o functie care sa stearga lista de la ex 3
my_list = [] #PRIN SUPRASCRIERE
print(my_list)

#7. Copy paste la ex 5. Verifica inca o data.

if not my_list:
    print("Lista este goala.")
else:
    print("Lista nu este goala")

# 8. Avand dictionarul dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
# Foloseste o functie ca sa afisezi Elevii (cheile)
my_dict = {
    'Ana' : 8,
    'Gigel' : 10,
    'Dorel' : 5
}
print (my_dict.keys())

#9. Printeaza cei 3 elevi si notele lor
    # EX: 'Ana a luat nota {x}
    # Doar nota o vei lua folosindu te de cheie

# print(my_dict['Ana', 'Gigel', 'Dorel'])
# print(my_dict.keys(), " a luat nota ", (my_dict['Ana']))
# print(my_dict['Ana'])
# print(my_dict.items())
#for = insiruieste keys
# item[0] - incepand de la item(NU INDEX) 0 (cheia 0, cazul de fata 'Ana'
# item [1] - atasand item 1 (cheia 1, cazul de fata '8'
for item in my_dict.items():
    print(item[0], " a luat nota ", item[1])

#10. Dorel a facut contestatie a primit 6
# Modifica nota lui Dorel in 6
# Printeaza nota dupa modificare
my_dict['Dorel'] = 6
print(my_dict['Dorel'])
#11. Gigel se transfera din clasa
# Cauta o functie care sa il stearga
# ● Vine un coleg nou. Adaugă Ionică, cu nota 9
# ● Printează noii elevi
del my_dict['Gigel']
print(my_dict)

my_dict["Ionica"] = 9

print(my_dict)

#todo lista l=[1,1,2,3,1,4,4,5,6,2] CUM ELIMINAM DUPLICATELE

l=[1,1,2,3,1,4,4,5,6,2]
l = list(set(l)) # set are prop de a nu accepta duplicate
print(l)
#TO DO
my_d={'a':{'aa': 11, 'ab': 12}, 'c': {'ca': 31}}
#1. returna valoarea cheii 'ab' din interiorul cheii a, de nu exista, sa se afiseze mesaj.
print(my_d['a']['ab'])
# 2. Cum return valoarea cheii 'b', iar daca nu exista, afis mesaj
print(my_d.get('b', 'Cheia nu exista!'))
#3. Cum return val cheii 'cb' din int cheii 'c', afis mesaj if neg
# print(my_d.get['c']['cb'])
intermediate_dict = my_d.get('c')
print(intermediate_dict.get('cb', 'Cheia nu exista'))
#&
print(my_d.get('c').get('cb', 'Cheia nu exista'))
#4. Return val cheii 'ba' din cheia 'b', afis mesaj if neg
print(my_d.get('b', 'Cheia nu exista'))
print(my_d.get('b').get('ba', 'Cheia nu exista'))
print(my_d.get('b', {}).get('ba', 'Cheia nu exista'))
