import random


my_move = input("enter your move: ")
opponents_move = random.randint(1, 4)
print ("the opponents move is: " + str(opponents_move))

match my_move:
    case "1" :
        if opponents_move == 1 or opponents_move == 2 :
              print("draw")
        elif opponents_move == 3 or 4:
             print ("I won")
        elif opponents_move == 5 or 6:
             print ("opponent won")
    case "2":
         if opponents_move == 1 or opponents_move == 2:
            print("draw")
         elif opponents_move == 3 or 4:
             print ("I won")
         elif opponents_move == 5 or 6:
             print ("opponent won")
    case "3":
        if opponents_move == 1 or opponents_move == 2:
            print("opponent won")
        elif opponents_move == 3 or 4:
             print ("draw")
        elif opponents_move == 5 or 6:
             print ("I won")
    case "4":
        if opponents_move == 1 or opponents_move == 2:
            print("opponent won")
        elif opponents_move == 3 or 4:
             print ("draw")
        elif opponents_move == 5 or 6:
             print ("I won")
    case "5":
        if opponents_move == 1 or opponents_move == 2:
            print("I won")
        elif opponents_move == 3 or 4:
             print ("opponent won")
        elif opponents_move == 5 or 6:
             print ("draw")
    case "6":
        if opponents_move == 1 or opponents_move == 2:
            print("I won")
        elif opponents_move == 3 or 4:
             print ("opponent won")
        elif opponents_move == 5 or 6:
             print ("draw")