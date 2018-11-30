class Package:
    __price = 0.0
    volume = 0.0
    material = ""
    __producer = ""
    package_type = None

    def __init__(self, price, producer, material, volume):
        self._price = price
        self._producer = producer
        self.material = material
        self.volume = volume
