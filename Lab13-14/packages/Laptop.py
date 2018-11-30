from packages.Package import *
from enums.ComputerType import *

class Laptop(Package):
    package_type = ComputerType.LAPTOP
    type_of_cap = ""


    def __init__(self, price, producer, material, volume, type_of_cap):
        self._price = price;
        self._producer = producer;
        self.material = material
        self.volume = volume
        self.type_of_cap = type_of_cap


    def __str__(self):
        return "Type of computer:"+ str(self.package_type) +" Price: " + str(self._price) + "  Producer: " + str(
            self._producer) + " Material: " + self.material + " Volume: " + str(self.volume)+" Type of cap: " + str(self.type_of_cap)
