class Road:

    def __init__(self, length, width):
        self.length = length
        self.width = width
        self.mass_in_sgm = 25
        self.height = 5

    def all_mass(self):
        all_mass = (self.length * self.width * self.mass_in_sgm * self.height) / 1000
        return print(f'Масса асфальта, необходимая для покрытия всего дорожного полотна: {all_mass}' )


r = Road(20, 5000)
r.all_mass()

