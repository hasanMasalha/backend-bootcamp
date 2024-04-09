import generate_board
def get_next_board(board):
    new_board = generate_board.get_empty_board()

    for i in range(0,len(board)):
        for j in range(0,len(board)):
            neighbours_counter = 0
            if j+1 <8:
                if board[i][j+1] == 1  : 
                    neighbours_counter+=1
            if j-1 >= 0:
                if board[i][j-1]==1 :
                    neighbours_counter+=1
            if i+1<8 :
                if board[i+1][j] == 1:
                    neighbours_counter+=1
            if i-1 <=0:
                if board[i-1][j]==1:
                    neighbours_counter+=1
            if i +1 <8 and j+1 <8:
                if board[i+1][j+1]==1 :
                    neighbours_counter+=1
            if j-1>=0 and i-1 >=0:
                if board[i-1][j-1]==1:
                    neighbours_counter+=1
            if i+1<8 and j-1 >=0:
                if board[i+1][j-1]==1:
                    neighbours_counter+=1
            if i-1 >=0 and j+1 <8:
                if board[i-1][j+1]==1 :
                    neighbours_counter+=1
            if board[i][j] == 0 and neighbours_counter == 3:
                new_board[i][j]= 1
            if board[i][j] == 1 and neighbours_counter >3:
                new_board[i][j]= 0 
            if board[i][j] == 1 and (neighbours_counter ==2 or neighbours_counter==3):
                new_board[i][j] = 1
            if board[i][j] == 1 and neighbours_counter <2:
                new_board[i][j]= 0 
    return new_board
        
