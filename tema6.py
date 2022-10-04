# 1.
# Clasa Cerc
#
# Atribute: raza, culoare
#
# Constructor pt ambele atribute
#
# Metode:
# descrie_cerc() - va PRINTA culoarea si raza
# aria() - va RETURNA aria
# diametru()
# circumferinta()

class Cerc:

    raza = None
    culoare = None

    def __init__(self, raza, culoare):
        self.raza = raza
        self.culoare = culoare

    def descriere_cerc(self):
        print(self.raza, self.culoare)

    def aria(self):
        return 3.14 * self.raza * self.raza
    def diametru(self):
        return 2 * self.raza
    def circumferinta(self):
        return 2 * 3.14 * self.raza



cerc1 = Cerc(10, "Rosu")
cerc2 = Cerc(5, "Albastru")
cerc1.descriere_cerc()
print(cerc1.aria())
print(cerc2.aria())
cerc2.descriere_cerc()
print(cerc1.diametru())
print(cerc2.diametru())
print(cerc1.circumferinta())
print(cerc2.circumferinta())
# print(cerc.raza, cerc.culoare)


# 2.
# Clasa Dreptunghi
#
# Atribute: lungime, latime, culoare
#
# Constructor pt toate atributele
#
# Metode:
# descrie()
# aria()
# perimetrul()
# schimba_culoarea(noua_culoare) - aceasta metoda nu returneaza nimic.
# Ea va lua ca si param o noua culoare si va suprascrie atributul self.culoare.
# Puteti verifica schimbarea culorii prin apelarea metodei descrie().

class Dreptunghi:
    lungime = None
    latime = None
    culoare = None

    def __init__(self, lungime, latime, culoare):
        self.lungime = lungime
        self.latime = latime
        self.culoare = culoare

    def descriere(self):
        print(self.lungime, self.latime, self.culoare)
    def aria(self):
        return self.lungime * self.latime
    def perimetru(self):
        return 2 * self.lungime + 2 * self.latime
    def schimba_culoare(self, noua_culoare):
        self.culoare = noua_culoare



dreptunghi = Dreptunghi(10, 5, "Alb")
dreptunghi.descriere()
print(dreptunghi.aria())
print(dreptunghi.perimetru())
dreptunghi.schimba_culoare("Verde")
dreptunghi.descriere()

# 3.
# Clasa Angajat
#
# Atribute: nume, prenume, salariu
#
# Constructor pt toate atributele
#
# Metode:
# descrie()
# nume_complet()
# salariu_lunar()
# salariu_anual()
# marire_salariu(procent)

class Angajat:
    nume = None
    prenume = None
    salariu = None

    def __init__(self, nume, prenume, salariu):
        self.nume = nume
        self.prenume = prenume
        self.salariu = salariu

    def descriere(self):
        print(self.nume, self.prenume, self.salariu)
    def nume_complet(self):
        return self.nume + " " + self.prenume
    def salariu_lunar(self):
        return self.salariu
    def salariu_anual(self):
        return self.salariu * 12
    def marire_salariu(self, procent):
        self.salariu = self.salariu + procent / 100 * self.salariu



angajat = Angajat("Volar", "Vicentiu", 5700)
angajat.descriere()
print(angajat.nume_complet())
print(angajat.salariu_lunar())
print(angajat.salariu_anual())
angajat.marire_salariu(20)
print(angajat.salariu_lunar())

# 4.
# Clasa Cont
#
# Atribute: iban, titular_cont, sold
#
# Constructor pentru toate
#
# Metode:
# afisare_sold() - Titularul x are in contul y suma de n lei
# debitare_cont(suma)
# creditare_cont(suma)

class Cont:

    IBAN = None
    titular_cont = None
    sold = None

    def __init__(self, IBAN, titular_cont, sold):
        self.IBAN = IBAN
        self.titular_cont = titular_cont
        self.sold = sold
    def afisare_sold(self):
        print("Titularul ", self.titular_cont, " are in contul ", self.IBAN,  " suma de ", self.sold, " lei.")
    def debitare_cont(self, suma):
        self.sold = self.sold - suma
    def creditare_cont(self, suma):
        self.sold = self.sold + suma



cont = Cont ("RO123456789", "A", 120)
cont.afisare_sold()
cont.debitare_cont(40)
cont.afisare_sold()
cont.creditare_cont(30)
cont.afisare_sold()

#5.
# Clasa Factura
#
# Atribute: seria (va fi constanta, nu trebuie constructor, toate facturile vor avea aceeasi serie), numar, nume_produs, cantitate, pret_buc
#
# Constructor: toate atributele, fara serie
#
# Metode:
# schimba_cantitatea(cantitate)
# schimba_pretul(pret)
# schimba_nume_produs(nume)
# genereaza_factura() - va printa tabelar daca reusiti
#

class Factura:
    seria = None
    numar = None
    nume_produs = None
    cantitate = None
    pret_buc = None

    def __init__(self, seria, numar, nume_produs, cantitate, pret_buc):
        self.seria = seria
        self.numar = numar
        self.nume_produs = nume_produs
        self.cantitate = cantitate
        self.pret_buc = pret_buc

    def schimba_cantitatea(self, cantitate):
        self.cantitate = cantitate

    def schimba_pretul(self, pret):
        self.pret_buc = pret

    def schimba_nume_produs(self, nume):
        self.nume_produs = nume

    def genereaza_factura(self, nume, cantitate, pretbuc):
        print("Produs" , "|" ,"Cantitate", "|" ,"Pret Bucata","|", "Total")
        print(self.nume_produs,  " | " , self.cantitate, " "," ", " " ," | " , self.pret_buc, " ", " ", " ", " | " , self.cantitate * self.pret_buc)
factura = Factura("RO0987", 101, "Covor", 3, 200)
print("Factura", factura.seria, "Numar", factura.numar)
from datetime import date
today = date.today()
print("Data: ", today)
factura.genereaza_factura("Cana", 4, 28)





