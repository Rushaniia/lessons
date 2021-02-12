class Example(Exception):
    def __init__(self, *args):
        self.my_list = []

    def func_str(self, my_list):
        try:
            for el in self.my_list:
                if type(el) == type('1'):
                    raise Example ('В списке присутствует элемент типа "str"')

        except Example as ex:
            print('Не число!', ex)

    def div(self, my_list):
        while True:
            try:
                value = input('Введите число в список: ')
                if value == 'q':
                    break
                if not value.isdigit():
                    raise Example(value)
                my_list.append(int(value))
            except Example as ex:
                print('Не число!', ex)


my_list = [1, 2, "3"]
print("Введенный список: ", my_list, "\n")
e = Example([1, 2, "3"])
e.func_str(my_list)
e.div(my_list)
print("Новый список: ", my_list, "\n")
