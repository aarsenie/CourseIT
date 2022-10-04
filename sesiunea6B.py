# # MOSTENIRE,,  ABSTRACTIZARE, POLIMORFISM, ENCAPSULARE
# #----->
# ### CELE 4 PRINCIPII DE BAZA AI OOP
#
# ###INHERITANCE
#
# ## presupune o clasa parinte si o clasa copil care mosteneste de la parinte
# ## MOSTENESTE: toate ATRIBUTELE & METODELE
# class Bird:
#     def __init__(self):
#         self.name = 'Birdy'
#         print("Bird created")
#     def who_am_i(self):
#         print("I am a bird")
#     def fly(self):
#         print("I am flying")
#
# class Penguin(Bird):        # clasa copil
#     def __init__(self):
#         super().__init__() # initializam clasa parinte
#         print("Penguin created")
#         self.name = "Penguin"
#
#     def who_am_i(self):
#         print("I am a penguin")
#
#     def swim(self):
#         print("I am swimming")
#
# pengu = Penguin()
# pengu.who_am_i()
# pengu.swim()
# pengu.fly()
# #
# # class Person
# #
# # class Student(Person)
# #
# # class Freshman(Person)
# #
# #
# # class Employee(Person)
# ## tot o persoana
#
#
# ### POLYMORPHISM
#
# ### Permite obiectelor sa ia mai multe forme
# ### Prin creearea unei INTERFETE comune
#
# class Romania:
#     def language(self):
#         print("In Romania the spoken language is romanian")
#     ## deschide un site
#     ## pe site cauta tara
#     ## returneaza limba
# class USA:
#     def language(self):
#         print("In the USA the spoken language is english")
#
# #INTERFATA COMUNA:
#
# def what_do_they_speak(country):
#     country.language()
#
# ro = Romania()
# us = USA()
# what_do_they_speak(ro)
# what_do_they_speak(us)
#
#
# #ABSTRACTION:
#
# ## SE ASCUNDE fata de USER functionalitatea interna a unei metode
# ## oferindu i acestuia doar informatia asupra CE face metoda, nu si CUM se face
#
#
# from abc import ABC, abstractmethod
#
# class Car(ABC):
#     # METODA NORMALA
#     def description(self):
#         print("Your object is a car")
#
#     @abstractmethod #abstractizare, nu oferim implementarea
#     def top_speed(self):  #fiecare copil al clasei Car va trb sa implementeze top_speed
#         raise NotImplementedError
#         # FIE->/
#             #PASS
#
# class Dacia(Car):
#     def top_speed(self):
#         print("The top speed is 240km/h")
#
#
# class Tesla(Car):
#     def top_speed(self):
#         print("The top speed is 250km/h")
#
#
# class BMW(Car):
#     pass
#
# dacia = Dacia()
# dacia.description()
# dacia.top_speed()
# tesla = Tesla()
# tesla.description()
# tesla.top_speed()
# # bmw = BMW()
# # bmw.description()
# # bmw.top_speed()
#
# # ENCAPSULARE: concept OOP prin care se ascunde accesul la date din exterior
#
# ## modificarea se face DOAR dintr-un singur LOC
# ## PRIN INTERMEDIUL UNEI METODE
#
# class Computer:
#     def __init__(self):
#         self.__price = 1000  ## Atribut PRIVATE
#
#     def set_price(self, new_price):
#         self.__price = new_price
#
#     def get_price(self):
#         print(self.__price)
#     def __hidden(self):
#         print("I am hidden")
#     def call_hidden(self):
#         self.__hidden()
#
# c1 = Computer()
# c1.get_price()
# c1.set_price(2000)
# c1.get_price()
# c1.call_hidden()
#
# # mai exista si atribute protected, similare cu cele private (au doar o _ in fata numelor)
#
# # dar spre deosebire de private, ele pot fi apelate din afara clasei, insa conventia e sa nu...
#
# class Dog:
#     def __init__(self):
#         self.name = "Rex" # atribute protected
#         self.__age = 5
#
# doggy = Dog()
# print(doggy.name) # merge, desi nu indicat
# # print(doggy.__age) ##eroare
#
# # presupunem o class Person cu 2 Atribute, name si age si o metoda
# # care afiseaza <name> si <age> years old.
#
# # Si mai avem o clasa Student, care evident ca e tot o persoana, dar are in plus 2 atribute, grade si scholarship (ambele float).
# # Clasa mai are si o metoda show_finance care returneaza valoarea bursei.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def describe(self):
        print(f"{self.name} is {self.age} years old.")

    def __str__(self):
        return f"{self.name} is {self.age} years old."

class Student(Person):

    def __init__(self, name, age, grade, scolarship):
        super().__init__(name, age)
        self.grade = grade
        self.scolarship = scolarship

    def show_finance(self):
        return self.scolarship

s1 = Student ("Alexandra", 21, 9.80, 1000)
s1.describe()
print(s1.show_finance())
s2 = Student("Gheorge", 19, 7.80, 800)
s2.describe()
print(s2.show_finance())

# Si inca o clasa Employee, care este o persoana angajata cu un rate
# (tarif pe ora in float) si un num_of_hours (numar de ore lucrate intr`o luna, int)
# Clasa mai are si o metoda show_finance care returneaza salariul
# pe care il obtine angajatul intr`o luna.

class Employee(Person):
    def __init__(self, name, age, rate, num_of_hours):
        super().__init__(name, age)
        self.rate = rate
        self.num_of_hours = num_of_hours

    def show_finance(self):
        return self.rate * self.num_of_hours

e1 = Employee ("Adela", 31, 40, 21.50)
e1.describe()
print(e1.show_finance())

# Acum, daca am avea un nou tip de persoana, si anume un WorkingStudent, care lucreaza, deci are atat salariu cat si bursa.
# Cum facem sa ii afisam finantele?

class WorkingStudent(Employee, Student): #MultipleINHERITANCE
    def __init__(self, name, age, rate, num_of_hours, grade, scholarship):
        Employee.__init__(self, name, age, rate, num_of_hours)
        Student.__init__(self, name, age, grade, scholarship)

    def show_finance(self):
        return self.rate * self.num_of_hours + self.scolarship

sara = WorkingStudent ("Sara",25, 40, 21.50, 8.5, 950)

