# OOP :
# 1. Concepte: - Clasa
#              - Obiect
#              - Atribute
#              - Metode/Functii

# 1. Clasa: - O categorie.
# 2. Obiect: - O entitate care apartine unei clase(categorii).
# 3. Atribute, Metode/Functii: un obiect este definit prin atribute, metode/functii.

class Animal:

    numar_picioare = None
    dieta = None
    natura = None # salbatic/domestic

    # in constuctor si in toate functiile definite in interiorul clasei, ca si argument va exista mereu acest SELF -> indica faptul
    # ca functia respectiva apartine de clasa in care este definita
    def __init__(self, numar_picioare, dieta, natura): # constructor. dupa cum ii sugereaza numele, cu aceasta metoda noi ne initializam un obiect care apartine acestei clase
        self.numar_picioare = numar_picioare
        self.dieta = dieta
        self.natura = natura

    # De fiecare data cand noi ne creem un nou obiect, intotdeauna prima data se apeleaza constructorul

caine = Animal(4, "carnivor", "domestic") # am creat variabila caine de tip Animal
print(caine.dieta)