import random
class alien:
    def __init__(self,name,materials):
        self.name=name
        self.materials = materials

earth_materials = [
    "Water",
    "Oxygen",
    "Silicon",
    "Iron",
    "Aluminum",
    "Carbon",
    "Gold",
    "Silver",
    "Copper",
    "Zinc",
    "Nickel",
    "Titanium",
    "Sodium",
    "Potassium",
    "Calcium",
    "Sulfur",
    "Phosphorus",
    "Nitrogen",
    "Hydrogen",
    "Quartz"
]
aliens_list = []
for i in range (1,5):
    declare = "alien" + str(i)
    small_list = []
    for j in range (1,3):
        choosen_material = random.choice(earth_materials)
        small_list.append(choosen_material)
    alien2=alien(declare,small_list)
    aliens_list.append(alien2)


mad_aliens = 0
for alien1 in aliens_list:
    for i in range(1,5):
        mat = random.choice(earth_materials)
        if mat in alien1.materials:
            earth_materials.remove(mat)
            print(alien1.name + " took "+ mat)
            break 
        elif mat not in alien1.materials:
            mat = random.choice(earth_materials)
            print(alien1.name + " didn`t take "+ mat)
        if i>=4:
            mad_aliens+=1

if mad_aliens<=1:
    print("succeded")
else:
    print("failed")

            



            
