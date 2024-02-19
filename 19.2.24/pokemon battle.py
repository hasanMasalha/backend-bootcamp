import random
class Player:
      def __init__(self, name, pokemons):
            self.name = name
            self.pokemons = pokemons

      def get_pokemon(self):
            choosen_pokemon = random.choice(self.pokemons)
            while choosen_pokemon.life<=0:
                  choosen_pokemon = random.choice(self.pokemons)
            return choosen_pokemon
                  
            
class Pokemon:
      def __init__(self,name,level,strength,speed,type,life=120):
            self.name=name
            self.level=level
            self.strength=strength
            self.speed=speed
            self.type=type
            self.life=life


player1=Player("hasan",[Pokemon("Charmander", 10, 8, 4, "fire"),
Pokemon("Bulbasaur", 8, 7, 3, "water"),
Pokemon("Squirtle", 9, 6, 5, "water"),
Pokemon("Pikachu", 12, 9, 5, "earth"),
Pokemon("Jigglypuff", 7, 5, 2, "wind")])

player2=Player("mohamed yousef",[Pokemon("Vaporeon", 11, 7, 6, "water"),
Pokemon("Geodude", 6, 8, 2, "fire"),
Pokemon("Alakazam", 15, 10, 5, "wind"),
Pokemon("Gyarados", 14, 9, 4, "water"),
Pokemon("Machamp", 13, 8, 3, "earth")])
print("let the fun begin!!!!")

player1Pokemon=random.choice(player1.pokemons)
player2Pokemon=random.choice(player2.pokemons)

firstPlayer= player1 if player1Pokemon.speed+random.randint(1,20) >= player2Pokemon.speed+random.randint(1,20) else player2
secondPlayer = player2 if firstPlayer == player1 else player1
firstPlayerPokemon = player1Pokemon if firstPlayer == player1 else player2Pokemon
secondPlayerPokemon = player2Pokemon if firstPlayer==player1 else player1Pokemon
player1_counter=0
player2_counter=0
winner_by_attack={
       "fire": ["water", "wind"],
       "water":["earth"],
       "earth":["fire","wind"],
       "wind":["water"]

}
def attack(attacker,defender):
    print("pokemon "+ attacker.name + " is attacking "+ defender.name)
    
    damage = 0
    if defender.type in winner_by_attack[attacker.type]: 
          damage = 2*(random.randint(1,20)+attacker.strength)
    else: 
          damage = (random.randint(1,20)+attacker.strength)
    print("damage = " + str(damage))
    defender.life -=damage
    print(defender.name +  " life now is: " + str(defender.life))
      

while(player2_counter <5 or player1_counter<5):
    if firstPlayerPokemon.life>=0:
        attack(firstPlayerPokemon,secondPlayerPokemon)
    else: 
        firstPlayerPokemon= firstPlayer.get_pokemon()
        player1_counter+=1
        attack(firstPlayerPokemon,secondPlayerPokemon)

    if  secondPlayerPokemon.life >=0:
        attack(secondPlayerPokemon,firstPlayerPokemon)
    else:
        secondPlayerPokemon=secondPlayer.get_pokemon()
        player2_counter+=1

        attack(secondPlayerPokemon,firstPlayerPokemon)

    
    
if player2_counter==5:
      print(firstPlayer.name + " won!!!")
if player1_counter == 5:
      print(secondPlayer.name + " won!!!")
            
