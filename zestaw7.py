class Punkt:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y
    @property
    def x(self):
        return self.__x
    @property
    def y(self):
        return self.__y
    def przesuń(self, dx, dy):
        self.__x += dx
        self.__y += dy
    def __repr__(self):
        return f"({self.__x}, {self.__y})"
    @classmethod
    def kopia(cls, punkt):
        return cls(punkt.__x, punkt.__y)

class Linia:
    def __init__(self, p1:Punkt = Punkt(), p2:Punkt=Punkt()):
        self.__p1 = Punkt.kopia(p1)
        self.__p2 = Punkt.kopia(p2)
    def przesuń(self, dx: float, dy: float):
        self.__p1.przesuń(dx, dy)
        self.__p2.przesuń(dx, dy)
    def __repr__(self):
        return f"linia: {self.__p1} --> {self.__p2}"
    @classmethod
    def kopia(cls, linia):
        return cls(linia.__p1, linia.__p2)
    @property
    def p1(self):
        return self.__p1
    @property
    def p2(self):
        return self.__p2

class Figura:
    def __init__(self, kolor:str):
        self.__kolor=kolor
    @property
    def kolor(self):
        return self.__kolor
    @kolor.setter
    def kolor(self,kolor):
        self.__kolor=kolor
    
class Trojkat(Figura):
    def __init__(self,kolor, p1:Punkt=Punkt(),  p2:Punkt=Punkt(), p3:Punkt=Punkt()):
        self.__l1=Linia(p1,p2)
        self.__l2=Linia(p2,p3)
        self.__l3=Linia(p1,p3)
        super().__init__(kolor)
    def __repr__(self):
        return f"Jestem {super().kolor} trójkątem:", {self.__l1}, {self.__l2}, {self.__l3}
    #def __str__(self):
        #return f"{self.__l1},{self.__l2},{self.__l3}"

class Czworokąt:
    def __init__(self, p1:Punkt=Punkt(), p2:Punkt=Punkt(), p3:Punkt=Punkt(), p4: Punkt = Punkt()):
        self.__l1 = Linia(p1, p2)  
        self.__l2 = Linia(p2, p3)
        self.__l3 = Linia(p3, p4)
        self.__l4 = Linia(p4, p1)
    def __repr__(self):
        return f"czworokąt: {self.__l1},{self.__l2},{self.__l3},{self.__l4}"

class Prostokąt(Czworokąt):
    def __init__(self,kolor, p1:Punkt, p2:Punkt):
        lewy_górny=p1
        prawy_dolny=p2
        p3=Punkt(p1.x, p2.y)
        p4=Punkt(p2.x, p1.y)
        super().__init__(kolor)
    def __repr__(self):
        return "Kwadrat: " + super().__repr__()
        

class Kwadrat(Prostokąt):
    def __init__(self, kolor, środek: float = Punkt(), bok: float = Punkt()):
        lewy_górny  = Punkt(środek.x-bok/2, środek.y+bok/2)
        prawy_górny = Punkt(środek.x+bok/2, środek.y+bok/2)
        prawy_dolny = Punkt(środek.x+bok/2, środek.y-bok/2)
        lewy_dolny  = Punkt(środek.x-bok/2, środek.y-bok/2)
        super().__init__(kolor)
        super().__init__(lewy_górny, prawy_górny, prawy_dolny, lewy_dolny)

    def __repr__(self):
        return "Kwadrat: " + super().__repr__()



trojkat = Trojkat("czerwony", Punkt(2,2), Punkt(4,5), Punkt(6,1))
prostokat = Prostokąt("zielony", Punkt(7,3), Punkt(5,8))
kwadrat = Kwadrat("niebieski", srodek=Punkt(10,10), bok=6)
print(trojkat)
# Jestem czerwony trójka ̨t [Linia:(2,2)(4,5),Linia:(4,5)(6,1),Linia:(6,1)(2,2)]
print(prostokat)
# Jestem zielony prostoka ̨t [Linia:(.,.)(.,.),Linia:(.,.)(.,.),Linia:(.,.)(.,.),Linia:(.,.)(.,.) print(kwadrat)
# Jestem niebieski kwadrat [Linia:(.,.)(.,.),Linia:(.,.)(.,.),Linia:(.,.)(.,.),Linia:(.,.)(.,.)