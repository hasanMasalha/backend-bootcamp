import random
my_matrix= [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]
for i in range(1,18):
    for j in range(0,2):
        x = random.randint(0,5)
        y=random.randint(0,5)
        while my_matrix[x][y]==0:
            x = random.randint(0,5)
            y=random.randint(0,5)
        if my_matrix[x][y]==0:
            my_matrix[x][y] = i
        w = random.randint(0,5)
        z=random.randint(0,5)
        while my_matrix[x][y]==0:
            w = random.randint(0,5)
            z=random.randint(0,5)
        if my_matrix[w][z]==0:
            my_matrix[w][z] = i
for i in range(0,5):
    for j in range(0,5):
        print(my_matrix[i])
     
