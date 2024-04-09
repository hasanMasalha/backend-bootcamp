import os
import time
import generate_board
import get_next_state

rounds_num = input("please enter how many rounds you want to play: ")

board= generate_board.get_empty_board()

first_board = generate_board.generate_init_board(board)
generate_board.print_board(first_board)
print("")
time.sleep(1)
os.system("cls")
next =get_next_state.get_next_board(first_board)
generate_board.print_board(next)
print("")
time.sleep(1)
os.system("cls")

for i in range(0,int(rounds_num)):
    next = get_next_state.get_next_board(next)
    generate_board.print_board(next)
    print("")
    time.sleep(1)
    os.system("cls")

