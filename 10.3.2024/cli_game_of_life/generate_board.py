
def get_empty_board():
    board = [[0 for _ in range(8)] for _ in range(8)]
    return board



def generate_init_board(board):
    living_cells = input("please enter with how many cells you want to start: ")
    for i in range (0,int(living_cells)):
        living_row = input("please enter the row of this living cell: ")
        living_col= input("please enter the column of this living cell: ")
        board[int(living_row)][int(living_col)]= 1
    return board

def print_board(board):
    for i in range(0,len(board)):
        for j in range(0,len(board)):
            print(board[i][j], end=" ")
        print("")