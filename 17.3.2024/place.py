import random
class place:
    def __init__(self, name, weapons: list):
        self.name = name
        self.weapons = weapons
    def get_weapons(self):
        return self.weapons

def generate_places() -> list:
    weapons_names = ["Revolver","Knife","Poison","Rope","Candlestick","Lead pipe","Wrench","Trophy","Axe","Poisoned dart"]
    places_names = ["Mansion","Library","Ballroom","Dining room","Study","Conservatory","Kitchen","Billiard room","Cellar","Garden","Observatory","Guest house","Hallway","Chapel","Attic","Theater","Swimming pool","Patio","Garage","Secret passage"]
    places=[]
    for this_place in places_names:
        weapons = []
        for i in range(0,5):
            this_weapon = random.choice(weapons_names)
            weapons.append(this_weapon)
        places.append(place(this_place,weapons))
    return places
