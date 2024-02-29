class item:
    def __init__(self,id,weight):
        self.weight = weight
        self.id=id
    def get_type(self):
        return "general item"


class bag:
    def __init__(self, id, weight_in = 0,items_num = []):
        self.id = id
        self.weight_in = weight_in
        self.items_num = items_num
    def add_item(self, item):
        if self.weight_in + item.weight <= 80 and len(self.items_num) < 6:
            self.weight_in += item.weight
            self.items_num.append(item)
        else:
            print("Sorry, you can't add this item to this bag!!!")

    def print_all(self):
        for bag_item in self.items_num:
            print(bag_item)
    def print_items_ny_category(self):
        category = input("please choose a category: ")
        for bag_item in self.items_num:
            if bag_item.get_type()==category:
                print(bag_item)

    def print_separated_by_category(self):
        items_dict = {}
        for bag_item in self.items_num:
            if bag_item.get_type() not in items_dict:
                items_dict[bag_item.get_type()] = []
                items_dict[bag_item.get_type()].append(bag_item)
            else: 
                 items_dict[bag_item.get_type()].append(bag_item)
        for k in items_dict :
            for item1 in items_dict[k]:
                print(item1.id)



class universal_charger(item):
    def __init__(self,id,weight,color,price,size,brand):
        self.color = color
        self.price = price
        self.size = size
        self.brand = brand
        item.__init__(self, id, weight)
    def get_type(self):
        return "universal_charger"



class passport(item):
    def __init__(self,id,weight,color,price,boughtFrom):
        self.color = color
        self.price = price
        self.boughtFrom = boughtFrom
        item.__init__(self,id,weight)
    def get_type(self):
        return "passport"


class sunglasses(item):
    def __init__(self,id,weight,color,haveCase,origin):
        self.color = color
        self.haveCase = haveCase
        self.origin = origin
        item.__init__(self,id,weight)
    def get_type(self):
        return(sunglasses)

class sneakers(item):
    def __init__(self,id,weight,brand,is_new,bought_from):
        self.brand = brand
        self.is_new = is_new
        self.bought_from = bought_from
        item.__init__(self,id,weight)

    def get_type(self):
        return "sneakers"
    
class Smartphone(item):
    def __init__(self,id,weight,brand,operating_system,storage,display,camera,materials):
        self.brand = brand
        self.operating_system = operating_system
        self.storage = storage
        self.display = display
        self.camera = camera
        self.materials = materials
        item.__init__(self,id,weight)
    def get_type(self):
        return "smartphone"


class campus(item):
    def __init__(self,id,weight,brand,accurancy,price,materials):
        self.brand = brand
        self.accurancy = accurancy
        self.price = price 
        self.materials = materials
        item.__init__(self,id,weight)
        def get_type(self):
            return "campus"





class smartwatch(item):
    def __init__(self,id,weight,brand,display,touchscreen,battery_life,heart_rate_monitor):
        self.brand = brand
        self.display = display 
        self.toutchscreen = touchscreen
        self.battery_life=battery_life
        self.heart_rate_monitor=heart_rate_monitor
        item.__init__(self,id,weight)
        def get_type(self):
            return "smartwatch"




def test_bag():
    # Creating items
    charger = universal_charger(1, 0.2, "Black", 15, "Medium", "BrandX")
    passport_item = passport(2, 0.1, "Blue", 10, "TravelMart")
    sunglasses_item = sunglasses(3, 0.3, "Red", True, "Italy")
    sneakers_item = sneakers(4, 0.5, "Nike", True, "ShoeMart")
    smartphone_item = Smartphone(5, 0.4, "Samsung", "Android", "128GB", "AMOLED", "Dual", "Metal and Glass")
    campus_item = campus(6, 0.6, "GraphingCo", "High", 50, "Plastic")
    smartwatch_item = smartwatch(7, 0.3, "Apple", "Retina", True, "2 days", True)

    # Creating a bag
    my_bag = bag(1)

    # Adding items to the bag
    my_bag.add_item(charger)
    my_bag.add_item(passport_item)
    my_bag.add_item(sunglasses_item)
    my_bag.add_item(sneakers_item)
    my_bag.add_item(smartphone_item)
    my_bag.add_item(campus_item)
    my_bag.add_item(smartwatch_item)

    # Printing all items in the bag
    print("All items in the bag: ")
    my_bag.print_all()

    # Printing items by category
    print("Items by category: ")
    my_bag.print_items_ny_category()

    # Printing items separated by category
    print("Items separated by category: ")
    my_bag.print_separated_by_category()


if __name__ == "__main__":
    test_bag()
