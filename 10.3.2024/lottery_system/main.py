import person
import raffle
import ticket 
import random


tickets_to_sell = []
people = []
current_partecipents_names = []
  #self,id,revenue,partecipents,max_num_of_people):
   # def __init__(self,id,raffle,price):

def get_raffle_details():
    max_num = input("please enter the max number of partecipents for this raffle: ")
    max_tickets = input("please enter the max number of tickets for this raffle: ")
    raffle_tickets = []
    for i in range(0,int(max_tickets)):
        tkt = ticket.ticket(i,20)
        raffle_tickets.append(tkt)
        tickets_to_sell.append(tkt)
    this_raffle= raffle.raffle(1,0,[],max_num,raffle_tickets)
    return this_raffle

def check_patrecipents_number(this_raffle: raffle.raffle, to_add: person.person):
    if len(this_raffle.partecipents)>= int(this_raffle.max_num_of_people):
        return False
    flag = False
    for part in this_raffle.partecipents:
        if to_add == part.name:
            flag == True
    if flag == False and  len(this_raffle.partecipents)< int(this_raffle.max_num_of_people):
        return True

def check_if_part(this_raffle: raffle.raffle, to_add):
    flag = False
    for per in this_raffle.partecipents:
        if per.name == to_add:
            flag = True
    return flag

def load_data(this_raffle : raffle.raffle):
    flag = True
    while flag == True:
        choice = input("please enter the buyer number, if you want to finish please enter Y: ")
        if choice == "Y" or tickets_to_sell == []:
            flag =False
        else:
            name = "person " + choice
            if check_if_part(this_raffle, name) == False:
                if check_patrecipents_number(this_raffle , name) == True:
                    try :
                        #if tickets_to_sell != None:
                        tkt_to_buy = random.choice(tickets_to_sell)
                        tickets_to_sell.remove(tkt_to_buy)
                        new_person = person.person(name,[])
                        new_person.add_ticket(tkt_to_buy)
                        this_raffle.partecipents.append(new_person)
                        this_raffle.revenue += tkt_to_buy.price
                    except ValueError as e: 
                        print("sorry cant buy a ticket :(")
                        flag = False     

            else:
                if tickets_to_sell != None:
                    try:
                        tkt_to_buy = random.choice(tickets_to_sell)
                        tickets_to_sell.remove(tkt_to_buy)
                        this_raffle.revenue += tkt_to_buy.price

                        for part in this_raffle.partecipents:
                            if part.name == name:
                                part.add_ticket(tkt_to_buy)
                    except ValueError as e: 
                        print("sorry there is no more tickets for sale")
        if flag == False:
            print("you cant enter more partecipents!!")      
        
def spin(this_raffle: raffle.raffle):
    winner = random.choice(this_raffle.tickets)
    for part in this_raffle.partecipents:
        if winner in part.tickets:
            print("winner winner chicken dinner !!!!")
            print("our winner is: "+ part.name)



def main():
    current_raffle =get_raffle_details()
    load_data(current_raffle)
    spin(current_raffle)

    


if __name__ == "__main__":
    main()