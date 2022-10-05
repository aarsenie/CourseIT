# 2. Faceti exercitiul dupa ce ati urcat proiectul (tot ce am facut pana acum impreuna)
#
# ABSTRACTION
# Clasa abstracta FormaGeometrica
# Contine un field PI=3.14
# Contine o metoda abstracta aria (optional)
# Contine o metoda a clasei descrie() - aceasta printeaza pe ecran ‘Cel mai probabil am colturi’

from abc import ABC, abstractmethod

class FormaGeometrica(ABC):
    # pi = 3.14
    def __init__(self):
        self.pi = 3.14

    @abstractmethod
    def arie(self):
        pass


    def descriere(self):
        print('Cel mai probabil am colturi')



class Patrat(FormaGeometrica):
    def __init__(self,latura):
        super().__init__()
        self.__latura = latura
        print(f'In initul clasei patrat, pi= {self.pi}')

    def arie(self):
        return self.__latura**2

    @property
    def latura(self):
        return self.__latura


    # @latura.setter
    def set_latura(self, new_latura):
        self.__latura = new_latura

    @latura.getter
    def get_latura(self):
        return self.__latura

    @latura.deleter
    def del_latura(self):
        self.__latura = None
        print('Am sters latura')



class Cerc(FormaGeometrica):
    def __init__(self, raza):
        super().__init__()
        self.__raza = raza
    def arie(self):
        return self.pi*(self.__raza**2)

    @property
    def raza(self):
        return self.__raza

    @raza.setter
    def set_raza(self, new_raza):
        self.__raza = new_raza

    @raza.getter
    def get_raza(self):
        return self.__raza

    @raza.deleter
    def del_raza(self):
        self.__raza = None
        print('Am sters raza')

    def descriere(self):
        print('Eu nu am colturi')

def descriere_interfata(obj):
    obj.descriere()

p1 = Patrat(3)
p1.descriere()
descriere_interfata(p1)

print(f'Latura este {p1.latura}')
print(f'Aria este {p1.arie()}')
p1.set_latura(5)
print(f'Noua latura este {p1.get_latura}')
del p1.del_latura

c = Cerc(5)
c.descriere()
descriere_interfata(c)
print(f'Raza este {c.raza}')
print(f'Aria este {c.arie()}')
c.set_latura=8
print(f'Noua raza este {c.get_raza}')
del c.del_raza











