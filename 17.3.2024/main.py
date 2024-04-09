import random 
import person
import place

weapons = ["Revolver","Knife","Poison","Rope","Candlestick","Lead pipe","Wrench","Trophy","Axe","Poisoned dart"]
game_places = place.generate_places()

def generate_players():
    players = []
    for i in range (0,5):
        fav_weapons = []
        fav_places = [] 
        name = "person" + str(i)
        for i in range (0,3):
            weapon = random.choice(weapons)
            fav_weapons.append(weapon)
        current_person = person.person(name, fav_weapons,[] )
        players.append(current_person)
    return players


def player_visits(players: list, round: int):
        for player in players:
            places_to_visit= random.randint(0,3)
            for i in range(0,places_to_visit):
                place_visited = random.choice(game_places)
                new_place = {place_visited: round}
                player.visited.append(new_place)

def kill(players, murder, round):
    players_to_kill=[]
    places_to_kill =[]
    if murder.get_visited() != None:
        for place1 in murder.get_visited():
            for key,val in place1.items():
                  if val == round:
                    for weap in  murder.get_fav_weapons():
                        if weap in key.get_weapons():
                            places_to_kill.append(key)
        for player in players: 
              if player != murder:
                   for place1 in player.get_visited():
                        for key,val in place1.items():
                             if val== round:
                                for weap in  murder.get_fav_weapons():
                                    if weap in key.get_weapons():
                                       players_to_kill.append(player)
        try:
            killed  = random.choice(players_to_kill)
            print("player " + killed.name + " was killed")
            players.remove(killed)   
        except:
            print("no one wad killed this round")          
    return players
               
     

def round(players: list, murder: person.person,round ):
    player_visits(players,round)
    new_players = kill(players,murder,round)
    return new_players
        
def susbect(players,round):
    players_susbected = []
    for i in range(0,2):
        show_place = random.choice(game_places)
        print(show_place.name+ "was visited by: ")
        
        for player in players:
            for place1 in player.get_visited():
                for key,val in place1.items():
                    if key.name == show_place.name and val == round:
                        print(player.name)
                        players_susbected.append(player)
    try:
        player_fav_weapon = random.choice(players_susbected)
        print("the fav weapons for "+ player_fav_weapon.name +" are ")
        print(player_fav_weapon.get_fav_weapons())
    except:
        print("ERROR")
        print("there is no weapons to show")
        


     

def start_game():
    
    this_game_players = generate_players()
    print("welcome to the assassin game")
    print("we have five players and one of them is a murder your mission is to know how ois this murder")
    print("the players are: ")
    for player in this_game_players:
        print(player.name)
    murder  = random.choice(this_game_players)

    i=1
    game_over = False
    while game_over == False:
        round(this_game_players,murder,i)
        susbect(this_game_players,i )
        guess = input("please enter a number from 1 to 4 based of who you this the killer is: ")
        killer_guess = "person" + guess
        if murder.name == killer_guess:
             print("you won")
             game_over = True
        if len(this_game_players)==2:
            print("WERE DONE")
            print("GAME OVER")
            game_over = True
        i+=1
    


start_game()