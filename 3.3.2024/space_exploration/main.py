import random
import time
import math
import json
import json_handler
import space_events
import space_ship

def main():
    saved_game = json_handler.load_game_data()
    game_events = ["Asteroid_Field","space_pirates","Black_Hole","Alien_Diplomacy"]
    if saved_game:
        player_spaceship = saved_game
        print("Welcome back to your space adventure!")
    else:
        name = input("Enter your spaceship's name: ")
        player_spaceship = space_ship.space_ship(name, fuel=100, health=100)
        print("Welcome to your space adventure!")

    while player_spaceship.health>=0:
        space_events.launch_spaceship(player_spaceship)
        space_events.explore(player_spaceship)
        my_event = random.choice(game_events)
        match my_event:
            case  "Asteroid_Field":
                 space_events.Asteroid_Field(player_spaceship)
            case "space_pirates":
                space_events.space_pirates(player_spaceship)
            case "Black_Hole":
                space_events.Black_Hole(player_spaceship)
            case "Alien_Diplomacy" :
                space_events.Alien_Diplomacy(player_spaceship)
 
        print(player_spaceship)
        json_handler.save_game(player_spaceship)
    print("Game over! Your spaceship was destroyed.")

main()


