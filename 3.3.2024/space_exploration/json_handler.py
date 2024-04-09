import json
import space_ship

def save_game(space_ship):
    data = {
        "name": space_ship.name ,
        "health": space_ship.health ,
        "fuel" : space_ship.fuel
    }
    with open("game_data.json", "w") as file:
        json.dump(data, file)
    print("Game data saved successfully.")

def load_game_data():
    try:
        with open("game_data.json", "r") as file:
            data = json.load(file)
            return space_ship.Space_ship(data["name"], data["fuel"], data["health"])
    except FileNotFoundError:
        print("No saved game data found.")
        return None
