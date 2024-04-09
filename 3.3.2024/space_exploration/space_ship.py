class space_ship:
    def __init__(self,name,fuel,health):
        self.name = name
        self.fuel = fuel
        self.health = health

    def __str__(self):
        return f"Spaceship: {self.name}\nFuel: {self.fuel}\nHealth: {self.health}"
    