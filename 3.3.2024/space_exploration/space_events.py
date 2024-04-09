import random
import space_ship

def launch_spaceship(space_ship):
     print("hello "+ space_ship.name + "we are launching")

def explore(space_ship):
     print(space_ship.name + " is exploring the space. ")
def Asteroid_Field(space_ship):
    print("you are facing an Asteroid Field")
    print("to avoid it press 1 ")
    print("to fire at the asteroids press 2 ")
    choice = input("please make a decision: ")
    if choice == 1:
        print("we avoided it successfully :) ")
    elif choice == 2: 
        print("we can handle this ")
        damage = random.randint(0,30)
        print("we made it, but the damage is: " + str(damage))
        space_ship.health -=  damage
    else:
        print("we dont know what to di !!!!")
        damage = random.randint(15,40)
        print("we made it, but the damage is: " + str(damage))
        space_ship.health -=  damage
def space_pirates(space_ship):
    print("you are facing space pirates")
    print("to avoid it and hide press 1 ")
    print("to attack them press 2 ")
    print("to Negotiate with them press 3 ")
    choice = input("please make a decision: ")
    if choice == 1:
        print("hw are hiding shhhhhh")
        print("we made it !!")
    elif choice == 2:
        print("we are attacking ")
        destiny = random.randint(0,1)
        if destiny == 1 :
            print("we are handiling the situation!!!")
            damage = random.randint(20,50)
            print("we made it, but the damage is: " + str(damage))
            space_ship.health -=  damage
        elif destiny == 0 :
            print("we didn`t make it :( ")
            space_ship -= 100 
    elif choice == 3:
                print("we are negotiationg")
                print("we made it in peace")
    else: 
        print("we dont know what to do !!!")
        damage = random.randint(30,60)
        print("we made it, but the damage is: " + str(damage))
        space_ship.health -=  damage
def Black_Hole(space_ship):
    print("we are facing a black hole!!!")
    print("to avoid it and hide press 1 ")
    print("to go threw it press 2 ")
    choice = input("please make a decision: ")
    if choice == 1:
         print("we are avoiding it")
         print("we made it :)")
         fuel_coast = random.randint(0,40)
         space_ship.fuel -=fuel_coast
    elif choice == 2:
        print("were gonna dieeeee!")
        print(" OMG WE MADE IT")
        fuel_coast = random.randint(20,60)
        space_ship.fuel -=fuel_coast
    else:
         print("we dont know what to do!!!")
         fuel_coast = random.randint(40,80)
         space_ship.fuel -=fuel_coast
def Alien_Diplomacy(space_ship):
     print("we have to Negotiate with the aliens ")
     print("to negotiate press 1 ")
     print("to escape press 2")
     choice = input("please make a decision: ")
     if choice == 1 :
          print("they want 20% of our fuel ")
          space_ship.fuel = 0.8* space_ship.fuel
     elif choice == 2:
          print("we are escaping")
          space_ship.fuel = 0.6* space_ship.fuel
     else:
        print("we dont know what to do")
        print("they are attacking we have to escape")
        space_ship.fuel =  0.5* space_ship.fuel      
        space_ship.health =  0.8* space_ship.health
        print("we make it but it cost us alot")
    




         


