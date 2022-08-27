import os
import time

import numpy as np
import random

GOAL = (8, 8)
ENTRY = (1, 1)


def create_maze(size):
    board = np.zeros((size, size), dtype=int)
    board[0] = np.ones(size) * 8
    board[-1] = np.ones(size) * 8

    for c in board:
        c[0] = 1
        c[-1] = 1
    board[-2][-2] = 6
    for i in range(0, (size // 3) * size-1):
        row = random.randint(2, size - 2)
        col = random.randint(2, size - 2)
        board[row, col] = 1

    # Setting Exit Position
    board[GOAL[0]][GOAL[1]] = 3

    # Setting Entry Position
    board[ENTRY[0]][ENTRY[1]] = 4

    return board


def check_move(x, y):
    print(f'checking {bo[x][y]}')
    if x >= bo.shape[0] -1:
        return False
    if y >= bo.shape[0] -1:
        return False

    if bo[x][y] != 1 and bo[x][y] != 8 and bo[x][y] != -5:
        return True
    else:
        return False


def make_move(old, new):
    print(f'-----old is: {bo[old[0]][old[1]]}')

    if bo[new[0]][new[1]] == -1:
        bo[new[0]][new[1]] = 9

    if bo[new[0]][new[1]] == 0:
        bo[new[0]][new[1]] = 4
    if bo[new[0]][new[1]] == -2:
        bo[new[0]][new[1]] = -3

    if bo[old[0]][old[1]] == 4:
        bo[old[0]][old[1]] = -1

    elif bo[old[0]][old[1]] == 9:
        bo[old[0]][old[1]] = -2
    elif bo[old[0]][old[1]] == -3:
        bo[old[0]][old[1]] = -5


def Traverse(past, current):
    if current == GOAL:
        bo[current[0]][current[1]] = 11
        show_board()
        return
    # right, down, left, up
    scores = [-1] * 4

    moves = [0] * 4
    # move right
    if check_move(current[0], current[1]+1):
        old = current
        new = current[0], current[1]+1
        if bo[new[0]][new[1]] == -1:
            scores[0] += 1
        elif bo[new[0]][new[1]] == -2:
            scores[0] -= 2
        elif bo[new[0]][new[1]] == 0:
            scores[0] += 2
        if past == new:
            scores[0] -= 1
        if bo[new[0]][new[1]] == -4:
            scores[0] -= 3

        moves[0] = new
        # make_move(old, new)
        # show_board()
        # time.sleep(0.5)
        # os.system('cls')
        # DFS(old, new)
    else:
        scores[0] -= 5

    # move down
    if check_move(current[0] + 1, current[1]):
        old = current
        new = current[0] + 1, current[1]
        if bo[new[0]][new[1]] == -1:
            scores[1] += 1
        elif bo[new[0]][new[1]] == -2:
            scores[1] -= 2
        elif bo[new[0]][new[1]] == 0:
            scores[1] += 2
        if past == new:
            scores[1] -= 1
        if bo[new[0]][new[1]] == -4:
            scores[1] -= 3
        moves[1] = new
        # make_move(old, new)
        # show_board()
        # time.sleep(0.5)
        # os.system('cls')
        # DFS(old, new)
    else:
        scores[1] -= 5

    # move left
    if check_move(current[0], current[1] - 1):
        old = current
        new = current[0], current[1] - 1
        if bo[new[0]][new[1]] == -1:
            scores[2] += 1
        elif bo[new[0]][new[1]] == -2:
            scores[2] -= 2
        elif bo[new[0]][new[1]] == 0:
            scores[2] += 2
        if past == new:
            scores[2] -= 1
        if bo[new[0]][new[1]] == -4:
            scores[2] -= 3
        moves[2] = new
        print(f'---------New is: {new}')
        # make_move(old, new)
        # show_board()
        # time.sleep(0.5)
        # os.system('cls')
        # DFS(old, new)
    else:
        scores[2] -= 5

    # move up
    if check_move(current[0] - 1, current[1]):
        old = current
        new = current[0] - 1, current[1]
        if bo[new[0]][new[1]] == -1:
            scores[3] += 1
        elif bo[new[0]][new[1]] == -2:
            scores[3] -= 2
        elif bo[new[0]][new[1]] == 0:
            scores[3] += 2
        if past == new:
            scores[3] -= 1
        if bo[new[0]][new[1]] == -4:
            scores[3] -= 3
        moves[3] = new
        # make_move(old, new)
        # show_board()
        # time.sleep(0.5)
        # os.system('cls')
        # DFS(old, new)
    else:
        scores[3] -= 5

    bst_move = moves[scores.index(max(scores))]
    print(f'----------- Scores {scores}')
    print(f'----------- moves {moves}')
    print(f'----------- best move is {bst_move}')
    # bst_move = bst_move[0]

    if bst_move == 0:
        print(f'-------- No Possible Way-------')
        return
    make_move(current, bst_move)
    show_board()
    time.sleep(0.4)
    Traverse(current, bst_move)


def show_board():
    for row in bo:
        for rec in row:
            if rec == 0 or rec == -1 or rec == -2:
                print('-', end=' ')
            elif rec == -1 or rec == -2:
                print('-', end=' ')
            elif rec == -2:
                print('-', end=' ')
            elif rec == 1:
                print('|', end=' ')
            elif rec == 8:
                print('—', end='—')
            elif rec == 6:
                print('~', end=' ')
            elif rec == 4:
                print('A', end=' ')
            elif rec == 9:
                print('A', end=' ')
            elif rec == -3:
                print('A', end=' ')
            elif rec == 3:
                print('G', end=' ')
            elif rec == 11:
                print('O', end=' ')
            elif rec == -5:
                print('-', end=' ')
            else:
                print(rec, end=' ')

        print()


if __name__ == '__main__':
    bo = create_maze(10)
    show_board()

    Traverse((1, 1), (1, 1))
