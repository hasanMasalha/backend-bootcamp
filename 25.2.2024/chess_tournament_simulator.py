import random
class player:
    def __init__(self,name,ranking, total_points=0):
        self.name = name
        self.ranking = ranking
        self.total_points = total_points

class round:
    def __init__(self,player1,player2):
        self.player1 = player1
        self.player2 = player2
    
    def calculate_points(self):
            palyer_1_chance=0
            palyer_2_chance=0
            if self.player1.ranking > self.player2.ranking :
                ratio = 1-(self.player2.ranking/self.player1.ranking)
                palyer_1_chance = 0.4 + ratio
                palyer_2_chance = 0.4 - ratio 
            else :
                ratio = 1-(self.player1.ranking/self.player2.ranking)
                palyer_2_chance = 0.4 + ratio
                palyer_1_chance = 0.4 - ratio 

            results1= ["player1","player2","draw"]
            weights = [palyer_1_chance,palyer_2_chance,0.2]
            random_outcome = random.choices(results1, weights)[0]
            if random_outcome == "player1":
                self.player1.total_points +=1
            elif random_outcome == "player2":
                self.player2.total_points +=1 
            elif random_outcome == "draw":
                self.player2.total_points +=0.5
                self.player1.total_points +=0.5
class tournament:
    def __init__(self, players):
        self.players = players
    def start(self):
        for i in range (0,len(self.players)):
            for j in range(i+1,len(self.players)):
                if i != j:
                    round(self.players[i],self.players[j]).calculate_points()
                






players_enrolled = []
for i in range (0,4):
    name = "name"+str(i) 
    ranking = random.randint(1500,2000)
    players_enrolled.append(player(name,ranking))
    print(name + " " + str(ranking))
tournament1 = tournament(players_enrolled)
tournament1.start()
for one in players_enrolled:
    print(one.total_points)


    


    