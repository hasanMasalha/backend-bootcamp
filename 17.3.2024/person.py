class person:
    def __init__(self,name,fav_weapons : list, visited ):
        self.name= name
        self.fav_weapons = fav_weapons
        self.visited = visited
    def get_visited(self):
        return self.visited
    def get_fav_weapons(self):
        return self.fav_weapons
        
        