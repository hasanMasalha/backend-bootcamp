class person:
    def __init__(self,name,gender, age,profession, favorite_tv_show, favorite_food):
        self.name=name
        self.gender=gender
        self.age=age
        self.profession=profession
        self.tv_show=favorite_tv_show
        self.favorite_food=favorite_food



people = [person("hasan masalha", "male", 25, "software", "friends","pizza"),
          person("mohamad yousef","male",22,"body builder","game of thrones","salad"), 
          person("malak yoounis", "female", 21, "chef", "super man","green salad"),
          person("sama kayal","female",45,"waiter","suits","nurger"),
]
name1 = input("please enter the name: ")
gender1 = input("please enter the gender(M for male F for female): ")
age1 = int(input("please enter the age: "))
profession1 = input("please enter the profession: ")
favorite_tv_show1 = input("please enter the favorite tv show: ")
favorite_food1 = input("please enter the favorite food: ")
p = person(name1,gender1,age1,profession1,favorite_tv_show1,favorite_food1)
for user in people:
    flag = True
    if user.age - p.age > 10 or user.age - p.age < -10 : 
        flag = False
    if user.gender == p.gender:
        flag = False
    if flag == True:
        print(p.name + "in match with " + user.name)
    flag = True
if flag == False:
    print(p.name +"has no matches :(")


    
