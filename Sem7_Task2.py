class Road:
    def __init__(self, length, width):
        self.length = length
        self.width = width
        self.mass = 25  # kg/m2
        self.thickness = 0.05  # meters

    def calc_asphalt_mass(self):
        asphalt_mass = self.length * self.width * self.mass * self.thickness
        return asphalt_mass


road = Road(20, 5000)
asphalt_mass = road.calc_asphalt_mass()
print(f'Mass of asphalt needed = {asphalt_mass / 1000} tons')
