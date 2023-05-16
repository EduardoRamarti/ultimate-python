class Coordenadas:
    def __init__(self, lat, long):
        self.lat = lat
        self.long = long

    def __eq__(self, otro):  # equal
        return self.lat == otro.lat and self.long == otro.long

    def __ne__(self, otro):  # not equal
        return self.lat != otro.lat or self.long != otro.long

    def __lt__(self, otro):
        return self.lat + self.long > otro.lat + otro.long

    def __le__(self, otro):
        return self.lat + self.long <= otro.lat + otro.long


coords = Coordenadas(45, 27)
coords2 = Coordenadas(45, 27)
print(coords < coords2)
