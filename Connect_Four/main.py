
""" 
Kurt Bruckbauer
Connect_Four/main.py
5/20/20
Summary

 """
import numpy as np 

import math

# Game Constants
ROW = 6
COL = 7

BLUE = (0,0,255)
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255,255,0)

# Creates the game board
def game_board():
    board = np.zeros((ROW,COL))  # Zeroes = empty slots on game boara
    return board

def drop(board,row,col,piece):
    board[row][col] = piece

def valid_location(board, col):
    return board[ROW-1][col] == 0

def get_next_open_row(board, col):
    for row in range(ROW):
        if board[row][col] == 0:
            return row

def print_board(board):
    print(np.flip(board, 0)) # Flips the board \ otherwise game starts at (0,0) axis which is top left

def connect_four(board, piece):
    # Horizontal game board check for connect four
    for c in range(COL - 3):
        for r in range(ROW):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True
    
    # Vertical game board check for connect four
    for c in range(COL):
        for r in range(ROW - 3):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                return True

    # Diagonal UP board check for connect four
    for c in range(COL - 3):
        for r in range(ROW - 3):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                return True
    
    # Diagonal DOWN  board check for connect four
    for c in range(COL - 3):
        for r in range(3, ROW):
            if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                return True


board = game_board()
print_board(board)
game_over = False
turn = 0

while not game_over:
    # Prompt Player 1 Input
    if turn == 0: # if turn % is 0 than plyr1 turn else plyr2 turn
        col = int(input("Player 1 make your selection (0-6) "))

        if valid_location(board, col):
            row = get_next_open_row(board, col)
            drop(board,row,col,1)

            if connect_four(board, 1):
                print("Player 1 Wins !! ")
                game_over = True
                break

    else:
        # Prompt Plqyer 2 input
        col = int(input("Player 2 make your selection (0-6) "))

        if valid_location(board, col):
            row = get_next_open_row(board, col)
            drop(board,row,col,2)

            if connect_four(board, 1):
                print("Player 1 Wins !! ")
                game_over = True
                break

    turn += 1
    turn = turn % 2
    print_board(board)