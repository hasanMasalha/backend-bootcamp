import random
my_matrix= [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]
empty_matrix = [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]
nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
for i in nums:
    
        x = random.randint(0,5)
        y=random.randint(0,5)
        print(str(x) +" " + str(y))
        print(my_matrix[x][y])
        while my_matrix[x][y]!=0:
            x = random.randint(0,5)
            y = random.randint(0,5)
        my_matrix[x][y] = i
        print(my_matrix[x][y])
        w = random.randint(0,5)
        z=random.randint(0,5)
        while my_matrix[w][z]!=0:
            w = random.randint(0,5)
            z=random.randint(0,5)
        my_matrix[w][z] = i
        

     
def start(board, empty_one):
      choice1 =input("please enter a raw")
      choice2 = input("please enter a column")
      print("your choice is" + str(choice1)+ str(choice2))
      new_board = empty_one
      new_board[choice1][choice2] = board[choice1][choice2]
      for i in range(0,5):
          print(i)
      if new_board != board:
        start(board,new_board)
      else:
        print("congrats you win!!!")

    