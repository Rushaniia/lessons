from abc import ABC, abstractmethod

class Clothers(ABC):
    def __init__(self, name, param, cloth):
        self.name = name
        self.param = param
        self.cloth = cloth


    @abstractmethod
    def method1(self):
        print(f'\nТип одежды: ')

    @abstractmethod
    def method2(self):
        print(f'Параметры одежды: ')

    @abstractmethod
    def method3(self):
        print(f'Расход ткани: ')


class Suit(Clothers):
    def method1(self):
        super().method1()
        print('Костюм')

    def method2(self):
        super().method2()
        print('Рост')

    def method3(self):
        super().method3()
        return self.cloth * 2 + 0.3

class Coat(Clothers):
    def method1(self):
        super().method1()
        print('Пальто')

    def method2(self):
        super().method2()
        print('Размер')

    def method3(self):
        super().method3()
        return self.cloth / 6.5 + 0.5

class All_cloth:
    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2


    @property
    def all_cloth(self):
        return f'Всего необходимо ткани: {"%.2f" % float((self.value1 * 2 + 0.3) + (self.value2 / 6.5 + 0.5))}'


suit = Suit('Костюм', 170, 200)
coat = Coat('Пальто', 44, 50)
suit.method1()
print("%.2f" % suit.method3())
coat.method1()
print("%.2f" % coat.method3())

my_all_cloth = All_cloth(200,50)
print(my_all_cloth.all_cloth)






