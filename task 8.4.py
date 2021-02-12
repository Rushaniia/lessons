#task 8.4, 8.5, 8.6

class Sklad:
    def __init__(self):
        self._dict = {}

    def add_to(self, equipment):
        self._dict.setdefault(equipment.name, []).append(equipment)

    def extract(self, name):
        if self._dict[name]:
            self._dict.setdefault(name).pop(0)


class Equipment:
    def __init__(self, name, model, year, count):
        self.name = name
        self.model = model
        self.year = year
        self.count = count
        self.items = {'Наименование устройства': self.name, 'Модель': self.model, 'год производства': self.year, 'Количество': self.count}


    def __str__(self):
        return f'{self.model}-{self.year}-{self.count}'

    def income(self):
        try:
            name = input(f'Введите наименование: ')
            model = input(f'Введите модель: ')
            year = int(input(f'Введите год: '))
            count = int(input(f'Введите количество: '))
            item = {'Наименование устройства': name, 'Модель': model, 'год производства': year, 'Количество': count}
            self.items.update(item)
            print(self.items)
        except ValueError:
            print('Недопустимое значение!')


class Printer(Equipment):
    def __init__(self, name, model, year, count):
        super().__init__(name, model, year, count)

    def action(self):
        return 'Печатает'


class Scaner(Equipment):
    def __init__(self, name, model, year, count):
        super().__init__(name, model, year, count)

    def action(self):
        return 'Сканирует'


class Xerox(Equipment):
    def __init__(self, name, model, year, count):
        super().__init__(name, model, year, count)

    def action(self):
        return 'Копирует'


sklad = Sklad()
scaner = Scaner('Сканер', 'hp 1020', 2019, 1)
sklad.add_to(scaner)
scaner = Scaner('Сканер', 'hp 1021', 2020, 1)
sklad.add_to(scaner)
scaner = Scaner('Сканер', 'hp 1022', 2021, 2)
sklad.add_to(scaner)
printer = Printer('Принтер', 'sony 111', 2018, 3)
sklad.add_to(printer)
# выводим склад
print(sklad._dict)
# забираем с склада и выводим склад
sklad.extract('Сканер')
print()
print(sklad._dict)

Equipment.income(scaner)

