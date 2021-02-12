class Data:
    def __init__(self, data, month, year):
        self.data = data
        self.month = month
        self.year = year

    @classmethod
    def by_string(cls, data_by_string):
        day, month, year = map(int, data_by_string.split('-'))
        my_data = cls(day, month, year)
        print(cls, data_by_string)
        return my_data

    @staticmethod
    def valid(data_by_string):
        day, month, year = map(int, data_by_string.split('-'))
        if day <=31 and day != 0 and month <=12 and month != 0 and year <=2021:
            print(data_by_string)
            return day, month, year
        else:
            print('Ошибка!')

a = '10-02-2021'
print(Data.by_string(a))
print(Data.valid(a))