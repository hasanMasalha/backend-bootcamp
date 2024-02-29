class store:
    def __init__(self,id,workers,pets,balance):
        self.id=id
        self.workers = workers
        self.pets = pets
        self.balance=balance
    def pet_sold(self,pet):
        if pet.status !=  "broken" or  "in repair" :
            self.pets.remove(pet)
            self.balance += pet.price
    
    def broken_robot(self,pet):
        pet.status = "in repair"
        duration = input("please enter the duration for fixing this robot: 2")
        self.balance -= pet.cost_to_fix_per_day*int(duration)

    def update_palance_by_salary(self):
        for worker in self.workers:
            self.balance -= worker.salary
    def get_robot_by_id(self,id):
        for robot in self.pets:
            if robot.id == id:
                print(robot)
        for robot1 in self.workers:
            if robot1.id == id:
                print(robot1) 

    def pets_for_sale(self,min,max):
        for pet1 in self.pets:
            if isinstance(pet1,pet):
                if pet1.status == "for sale" and pet1.price < max and pet1.price >min:
                    print(pet1.name)
    def robots_repair(self):
        for worker in self.workers:
            if worker.status == "in repair":
                print(worker.name)
        for pet1 in self.pets:
            if pet1.status == "in repair":
                print(pet1.name)


                


class robot:
    def __init__(self,id,name,materials,cost_to_fix_per_day,status,battery):
        self.id = id
        self.name=name
        self.materials=materials
        self.battery=battery
        self.cost_to_fix_per_day=cost_to_fix_per_day
        self.status=status

class pet(robot):
    def __init__(self,id,name,materials,cost_to_fix_per_day,status,type,price,battery):
        self.type = type
        self.price = price
        robot.__init__(self,id,name,materials,battery,cost_to_fix_per_day,status)



class worker(robot):
    def __init__(self,id,name,materials,cost_to_fix_per_day,status,salary,battery):
        self.salary = salary        
        robot.__init__(self,id,name,materials,cost_to_fix_per_day,status,battery)
def test_store():
    # Creating a store
    my_store = store(1, [], [], 10000)

    # Creating some robots
    robot1 = robot(1, "Robot1", "Metal", 10, "for sale", 80)
    robot2 = robot(2, "Robot2", "Plastic", 15, "for sale", 90)

    # Creating some workers
    worker1 = worker(3, "Worker1", "Steel", 5, "working", 2000, 70)
    worker2 = worker(4, "Worker2", "Aluminum", 7, "in repair", 2500, 60)

    # Creating some pets
    pet1 = pet(5, "Pet1", "Circuit", 20, "for sale", "Robot", 500, 100)
    pet2 = pet(6, "Pet2", "Wires", 15, "in repair", "Robot", 400, 80)

    # Adding robots, workers, and pets to the store
    
    my_store.pets.append(pet1)
    my_store.pets.append(pet2)
    my_store.workers.append(worker1)
    my_store.workers.append(worker2)
    # Testing pet_sold method
    print("Balance before selling pet:", my_store.balance)
    my_store.pet_sold(pet1)
    print("Balance after selling pet:", my_store.balance)

    # Testing broken_robot method
    print("Status before repair:", pet2.status)
    my_store.broken_robot(pet2)
    print("Status after repair:", pet2.status)
    print("Balance after repair:", my_store.balance)

    # Testing update_balance_by_salary method
    print("Balance before updating by salary:", my_store.balance)
    my_store.update_palance_by_salary()
    print("Balance after updating by salary:", my_store.balance)

    # Testing get_robot_by_id method
    print("Robot with id 2:")
    my_store.get_robot_by_id(2)

    # Testing pets_for_sale method
    print("Pets for sale between 300 and 600:")
    my_store.pets_for_sale(300, 600)

    # Testing robots_repair method
    print("Robots in repair:")
    my_store.robots_repair()


if __name__ == "__main__":
    test_store()
