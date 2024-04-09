class person:
    def __init__(self,name,tickets : list):
        self.name=name
        self.tickets = tickets
    def add_ticket(self,ticket):
        self.tickets.append(ticket)
    def get_tickets(self):
        return self.tickets
                
