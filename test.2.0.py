# 2. Реализовать проект расчёта суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта — одежда, которая может иметь
# определённое название. К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для основных классов проекта,
# проверить на практике работу декоратора @property.
from abc import ABC, abstractmethod

# У вас есть два метода fabrik, сделайте из атрибутами через property и тогда в одежду можно добавить add, где будет self.fabrik + other.fabrik

class MyAbstractClass(ABC):
    @abstractmethod
    def fabrik(self):
        pass

class Clothes(MyAbstractClass):
    def __init__(self, name, param):
        self.name = name
        self.param = param

    def __add__(self, other):
        return Clothes(self.fabrik + other.fabrik)

    def __str__(self):
        return str(f'Мартка одежды: {self.name}, размер: {self.param}')

    def fabrik(self):
        pass

    def fabrik_summa2(self, other):
        result = self.fabrik + other.fabrik
        return result

    def fabrik_summa3(self, other, another):
        result = self.fabrik + other.fabrik + another.fabrik
        return result
class Coat(Clothes):

    @property
    def fabrik(self):
        result = self.param / 6.5 + 0.5
        return result

class Suit(Clothes):
    @property
    def fabrik(self):
        result = self.param / 6.5 + 0.5
        return result


c1 = Coat('Henderson', 6.5)
c2 = Coat('Zara', 4.5)
c3 = Coat('Zara', 6.5)
s1 = Suit('Oodji', 1)
print(c1)
print(c1.fabrik)
print(c2.fabrik)
print(c3.fabrik)
print(s1.fabrik)
print(Coat.fabrik_summa2(c1, c2))
print(Coat.fabrik_summa3(c1, c2, c3))


