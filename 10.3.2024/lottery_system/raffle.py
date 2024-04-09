class raffle:
    def __init__(self,id,revenue,partecipents: list,max_num_of_people,tickets):
        self.id = id
        self.revenue = revenue
        self.partecipents = partecipents
        self.max_num_of_people= max_num_of_people
        self.tickets = tickets
    def check_part_num(self,person_to_add):
        if self.max_num_of_people > len(self.partecipents):
            self.partecipents.append(person_to_add)
        else:
            print("sorry we have reached the max number of partecipents")
        

        
  