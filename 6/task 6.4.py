class Car:
    def __init__(self, name, color, speed, is_police=False):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police

    def go(self):
        return f'\nThe {self.name} went'

    def stop(self):
        return f'\nThe {self.name} stopped'

    def turn(self, direction):
        return f'\nThe {self.name} turned {direction}'

    def show_speed(self):
        return f'\nCar speed is {self.speed}'

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f'You were speeding! Your speed is {self.speed}'
        else:
            return f'Speed of {self.speed} is normal'


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f'You were speeding! Your speed is {self.speed}'
        else:
            return f'Speed of {self.speed} is normal'


class SportCar(Car):
    pass

class PoliceCar(Car):
    pass

my_town_car = TownCar('Ford', 'green', 75, False)
print(my_town_car.go(), my_town_car.show_speed(), my_town_car.stop())

my_work_car = WorkCar('Mazda', 'yellow', 30, False)
print(my_work_car.go(), my_work_car.turn('left'), my_work_car.show_speed(), my_work_car.stop())

my_sport_car = SportCar('Toyota', 'white', 100, True)
print(my_sport_car.go(), my_sport_car.turn('right'), my_sport_car.turn('left'), my_sport_car.show_speed(), my_sport_car.stop())

my_police_car = PoliceCar('BMV', 'black', 90, True)
print(my_police_car.go(), my_police_car.turn('right'), my_police_car.show_speed(), my_police_car.stop())