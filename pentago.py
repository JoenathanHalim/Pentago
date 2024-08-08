import numpy as np
import random


def display_board(board):
    # implement your function here
    print(board)  # To print the board in the console


def check_victory(board, turn, rot):
    # implement your function here
    h1 = 0
    v1 = 0
    d1 = 0
    s1 = 0

    h2 = 0
    v2 = 0
    d2 = 0
    s2 = 0
    draw2 = 0
    board_victory = board.copy()  # Copy dummy board to imitate before rotation

    if rot == 1:  # Rotate Q1 Clockwise
        board_victory[0:3, 3:6] = np.rot90(board_victory[0:3, 3:6], 1)
    elif rot == 2:  # Rotate Q1 Counter-Clockwise
        board_victory[0:3, 3:6] = np.rot90(board_victory[0:3, 3:6], 3)
    elif rot == 3:  # Rotate Q4 Clockwise
        board_victory[3:6, 3:6] = np.rot90(board_victory[3:6, 3:6], 1)
    elif rot == 4:  # Rotate Q4 Counter-Clockwise
        board_victory[3:6, 3:6] = np.rot90(board_victory[3:6, 3:6], 3)
    elif rot == 5:  # Rotate Q3 Clockwise
        board_victory[3:6, 0:3] = np.rot90(board_victory[3:6, 0:3], 1)
    elif rot == 6:  # Rotate Q3 Counter-Clockwise
        board_victory[3:6, 0:3] = np.rot90(board_victory[3:6, 0:3], 3)
    elif rot == 7:  # Rotate Q2 Clockwise
        board_victory[0:3, 0:3] = np.rot90(board_victory[0:3, 0:3], 1)
    elif rot == 8:  # Rotate Q2 Counter-Clockwise
        board_victory[0:3, 0:3] = np.rot90(board_victory[0:3, 0:3], 3)
    elif rot == 0:
        pass

    # Check situation before rotation
    h1 = victory_horizontal(board_victory)
    v1 = victory_vertical(board_victory)
    d1 = victory_diagonal(board_victory)
    s1 = victory_six(board_victory)
    # Check situation after rotation
    h2 = victory_horizontal(board)
    v2 = victory_vertical(board)
    d2 = victory_diagonal(board)
    s2 = victory_six(board)
    draw2 = draw_situation(board)

    # Return check results
    # Check for draw
    if h1 == 3 or v1 == 3 or d1 == 3 or s1 == 3:
        return 3
    elif h2 == 3 or v2 == 3 or d2 == 3 or s2 == 3:
        return 3
    elif draw2 == 3:
        return 3
    # AFTER PLACING BUT BEFORE ROTATION
    if (h1 == 1 or v1 == 1 or d1 == 1 or s1 == 1):  # Player 1 wins before rotation
        return 1
    # Player 2 wins before rotation
    elif (h1 == 2 or v1 == 2 or d1 == 2 or s1 == 2):
        return 2

    # AFTER ROTATION
    # Player 1 wins after and player 2 does not win rotation
    elif (h2 == 1 or v2 == 1 or d2 == 1 or s2 == 1):
        return 1
    # Player 2 wins and player 1 does not win after rotation
    elif (h2 == 2 or v2 == 2 or d2 == 2 or s2 == 2):
        return 2
    # Draw situation where either board is full after rotation or both player 1 and player 2 win after rotation
    else:  # No win / draw situation
        return 0


def victory_horizontal(board):  # Horizontal win
    win = 0
    for r in range(0, 6):
        counter1 = 0
        counter2 = 0
        for c in range(0, 5):
            if board[r, c] == 1:
                counter1 += 1
            if board[r, c] == 2:
                counter2 += 1
        if counter1 == 5 and counter2 != 5:
            win = 1
        elif counter2 == 5 and counter2 != 5:
            win = 2
        else:
            win = 3

    for r in range(0, 6):
        counter1 = 0
        counter2 = 0
        for c in range(1, 6):
            if board[r, c] == 1:
                counter1 += 1
            if board[r, c] == 2:
                counter2 += 1
        if counter1 == 5 and counter2 != 5:
            win = 1
        elif counter2 == 5 and counter2 != 5:
            win = 2
        else:
            win = 3

    return win


def victory_vertical(board):  # Vertical win
    win = 0
    for c in range(0, 6):
        counter1 = 0
        counter2 = 0
        for r in range(0, 5):
            if board[r, c] == 1:
                counter1 += 1
            if board[r, c] == 2:
                counter2 += 1
        if counter1 == 5 and counter2 != 5:
            win = 1
        elif counter2 == 5 and counter2 != 5:
            win = 2
        else:
            win = 3

    for c in range(0, 6):
        counter1 = 0
        counter2 = 0
        for r in range(1, 6):
            if board[r, c] == 1:
                counter1 += 1
            if board[r, c] == 2:
                counter2 += 1
        if counter1 == 5 and counter2 != 5:
            win = 1
        elif counter2 == 5 and counter2 != 5:
            win = 2
        else:
            win = 3
    return win


def victory_diagonal(board):  # Diagonal win
    win = 0
    counter1 = 0
    counter2 = 0
    for i in range(0, 5):
        if board[i, i] == 1:
            counter1 += 1
        if board[i, i] == 2:
            counter2 += 1
    if counter1 == 5 and counter2 != 5:
        win = 1
    elif counter2 == 5 and counter2 != 5:
        win = 2
    else:
        win = 3

    counter1 = 0
    counter2 = 0
    for i in range(1, 6):
        if board[i, i] == 1:
            counter1 += 1
        if board[i, i] == 2:
            counter2 += 1
    if counter1 == 5 and counter2 != 5:
        win = 1
    elif counter2 == 5 and counter2 != 5:
        win = 2
    else:
        win = 3

    counter1 = 0
    counter2 = 0
    for r in range(0, 5):
        if board[r, r + 1] == 1:
            counter1 += 1
        if board[r, r + 1] == 2:
            counter2 += 1
    if counter1 == 5 and counter2 != 5:
        win = 1
    elif counter2 == 5 and counter2 != 5:
        win = 2
    else:
        win = 3

    counter1 = 0
    counter2 = 0
    for c in range(0, 5):
        if board[c + 1, c] == 1:
            counter1 += 1
        if board[c + 1, c] == 2:
            counter2 += 1
    if counter1 == 5 and counter2 != 5:
        win = 1
    elif counter2 == 5 and counter2 != 5:
        win = 2
    else:
        win = 3

    counter1 = 0
    counter2 = 0
    for c in range(1, 6):
        if board[abs(c - 5), c] == 1:
            counter1 += 1
        if board[abs(c - 5), c] == 2:
            counter2 += 1
    if counter1 == 5 and counter2 != 5:
        win = 1
    elif counter2 == 5 and counter2 != 5:
        win = 2
    else:
        win = 3

    counter1 = 0
    counter2 = 0
    for c in range(0, 5):
        if board[abs(c - 5), c] == 1:
            counter1 += 1
        if board[abs(c - 5), c] == 2:
            counter2 += 1
        i = i - 2
    if counter1 == 5 and counter2 != 5:
        win = 1
    elif counter2 == 5 and counter2 != 5:
        win = 2
    else:
        win = 3

    counter1 = 0
    counter2 = 0
    i = 4
    for r in range(0, 5):
        if board[r, r + i] == 1:
            counter1 += 1
        if board[r, r + i] == 2:
            counter2 += 1
        i = i - 2
    if counter1 == 5 and counter2 != 5:
        win = 1
    elif counter2 == 5 and counter2 != 5:
        win = 2
    else:
        win = 3

    counter1 = 0
    counter2 = 0
    i = 4
    for r in range(1, 6):
        if board[r, r + i] == 1:
            counter1 += 1
        if board[r, r + i] == 2:
            counter2 += 1
        i = i - 2
    if counter1 == 5 and counter2 != 5:
        win = 1
    elif counter2 == 5 and counter2 != 5:
        win = 2
    else:
        win = 3

    return win


def victory_six(board):
    win = 0
    for c in range(0, 6):
        counter1 = 0
        counter2 = 0
        for r in range(0, 6):
            if board[r, c] == 1:
                counter1 += 1
            if board[r, c] == 2:
                counter2 += 1
        if counter1 == 6 and counter2 != 6:
            win = 1
        elif counter2 == 6 and counter2 != 6:
            win = 2
        else:
            win = 3

    for r in range(0, 6):
        counter1 = 0
        counter2 = 0
        for c in range(0, 6):
            if board[r, c] == 1:
                counter1 += 1
            if board[r, c] == 2:
                counter2 += 1
        if counter1 == 6 and counter2 != 6:
            win = 1
        elif counter2 == 6 and counter2 != 6:
            win = 2
        else:
            win = 3

    counter1 = 0
    counter2 = 0
    for r in range(0, 6):
        if board[r, r] == 1:
            counter1 += 1
        if board[r, r] == 2:
            counter2 += 1
    if counter1 == 6 and counter2 != 6:
        win = 1
    elif counter2 == 6 and counter2 != 6:
        win = 2
    else:
        win = 3

    counter1 = 0
    counter2 = 0
    for r in range(6, 0):
        if board[abs(r - 6), r] == 1:
            counter1 += 1
        if board[abs(r - 6), r] == 2:
            counter2 += 1
    if counter1 == 6 and counter2 != 6:
        win = 1
    elif counter2 == 6 and counter2 != 6:
        win = 2
    else:
        win = 3
    return win


def draw_situation(board):  # Draw Situation
    win = 0
    counter_draw = 0
    for r in range(0, 6):
        for c in range(0, 6):
            if board[r, c] == 1 or board[r, c] == 2:
                counter_draw += 1
    if counter_draw == 36:
        win = 3
    return win


def apply_move(board, turn, row, col, rot):
    # implement your function here
    board1 = board.copy()
    board1[row, col] = turn

    if rot == 1:  # Rotate Q1 Clockwise
        board1[0:3, 3:6] = np.rot90(board1[0:3, 3:6], 3)
    elif rot == 2:  # Rotate Q1 Counter-Clockwise
        board1[0:3, 3:6] = np.rot90(board1[0:3, 3:6], 1)
    elif rot == 3:  # Rotate Q4 Clockwise
        board1[3:6, 3:6] = np.rot90(board1[3:6, 3:6], 3)
    elif rot == 4:  # Rotate Q4 Counter-Clockwise
        board1[3:6, 3:6] = np.rot90(board1[3:6, 3:6], 1)
    elif rot == 5:  # Rotate Q3 Clockwise
        board1[3:6, 0:3] = np.rot90(board1[3:6, 0:3], 3)
    elif rot == 6:  # Rotate Q3 Counter-Clockwise
        board1[3:6, 0:3] = np.rot90(board1[3:6, 0:3], 1)
    elif rot == 7:  # Rotate Q2 Clockwise
        board1[0:3, 0:3] = np.rot90(board1[0:3, 0:3], 3)
    elif rot == 8:  # Rotate Q2 Counter-Clockwise
        board1[0:3, 0:3] = np.rot90(board1[0:3, 0:3], 1)
    elif rot == 0:
        pass
    return board1


def check_move(board, row, col):
    # implement your function here
    move = board[row, col]
    if row < 0 or row > 5 or col < 0 or col > 5:
        return False
    if move == 1:  # Player 1 has a marble there
        return False
    elif move == 2:  # Player 2 has a marble there
        return False
    elif move == 0:  # The spot is empty
        return True


def computer_move(board, turn, level):
    # implement your function here
    candidate_move = []
    candidate_move2 = []
    comp_win_move = []
    not_comp_win_move = []
    avoid_move = []
    board_comp = board.copy()
    win = 0
    # Check for possible moves for computer
    for row in range(0, 6):
        for col in range(0, 6):
            if board_comp[row, col] != 1 and board_comp[row, col] != 2:
                for rot in range(1, 9):
                    candidate_move.append((row, col, rot))

    if level == 1:  # Random move
        (row, col, rot) = random.choice(candidate_move)
    elif level == 2:
        for row, col, rot in candidate_move:
            board_2 = apply_move(board_comp, turn, row, col, rot)
            if (check_victory(board_2, turn, rot) == turn):  # Check if there is a winning move
                win = turn
                comp_win_move.append((row, col, rot))
                break
            # First 7 moves player cannot win in the following round
            elif (len(candidate_move) > 29 * 8):
                not_comp_win_move.append((row, col, rot))
            # Avoid move if it leads to suicide
            elif (check_victory(board_2, (3-turn), rot) == (3-turn)):
                avoid_move.append((row, col, rot))
            else:
                candidate_move2 = candidate_move.copy()
                for i in range(1, 9):
                    # Delete the occupied spot by computer
                    candidate_move2.remove((row, col, i))
                for row1, col1, rot1 in candidate_move2:
                    board_1 = apply_move(board_2, (3 - turn), row1, col1, rot1)
                    if (check_victory(board_1, (3 - turn), rot1) == (3 - turn)):
                        avoid_move.append(
                            (row, col, rot))  # Avoid move if it leads to player winning in the following round
                    elif (check_victory(board_1, (3-turn), rot1) == (3-turn)):
                        avoid_move.append((row, col, rot))  # Avoid suicide
        not_comp_win_move = [i for i in candidate_move if i not in avoid_move]
        # If player always win in next round (check mate), computer random move
        if (len(not_comp_win_move) == 0):
            not_comp_win_move = candidate_move.copy()
        if win == turn:  # If there is a winning move, play it
            (row, col, rot) = random.choice(comp_win_move)
        else:  # If there isn't, play the other move
            (row, col, rot) = random.choice(not_comp_win_move)
    return (row, col, rot)


def menu():
    game_board = np.zeros((6, 6))  # Set the game board to all-zeros
    print("Welcome to Pentago !")
    print("In order to proceed, please type a number that corresponds which one you want to play")
    while True:
        print("1. Game Rules")
        print("2. Play With Computer")
        print("3. Play with Another Player")
        print("Type 'Quit' to Quit")
        number = input("Please type a number you want to choose : ")
        if number == "1":
            print("")
            print("Pentago Rules :")
            print("1. This is a game consisting of 2 players")
            print(
                "2. Each player has their turn to put their marble in the 6x6 board with indices of column and row from 0 to 5 inclusively")
            print(
                "3. After a player put their marble in the 6x6 board, the player must rotate the board with indices from 1 to 8 inclusively")
            print(
                "4. The game stops with a win when a player has 5 consecutive marble diagonally, horizontally, or vertically")
            print(
                "5. The game stops with a draw when the boards are all filled with marbles but there are no 5 consecutive marble diagonally, horizontally, or vertically in the board")
            print("")
            while True:
                print("Type 'Quit' to quit")
                print("Type 'Back' to go back to the menu")
                print("")
                back = input("Please type your input ('Quit' or 'Back') : ")
                if back == "Back" or back == "Quit":
                    break
            if back == "Quit":
                break
        elif number == "2":
            display_board(game_board)
            print("Level 1 Computer : Easy")
            print("Level 2 Computer : Medium")
            print("Type 'Quit' to quit")
            while True:
                level = input(
                    "Please indicate which level you want to play (Type 1, 2, or 'Quit'): ")
                if level == "1":
                    level = int(level)
                    break
                elif level == "2":
                    level = int(level)
                    break
                elif level == "Quit":
                    level = int(level)
                    break
                else:
                    continue
            if level == "Quit":
                break
            while True:
                print("Type 'Quit' to Quit")
                turn = input(
                    "Please indicate your movement. Type 1 for player moves first, 2 for computer moves first : ")
                if turn == "1":
                    while True:
                        print("Player turn! Please indicate your movement.")
                        while True:
                            print("Type 'Quit' to Quit")
                            print("")
                            column1 = input(
                                "Player, please type the column you want to put your marble : ")
                            if column1 == "0" or column1 == "1" or column1 == "2" or column1 == "3" or column1 == "4" or column1 == "5":
                                break
                            elif column1 == "Quit":
                                number == "Quit"
                                break
                            else:
                                print(
                                    "Error! Please type a number between 0 to 5 inclusive")
                        if number == "Quit":
                            break
                        while column1 != "Quit":
                            print("Type 'Quit' to Quit")
                            print("")
                            row1 = input(
                                "Player, please type the row you want to put your marble : ")
                            if row1 == "0" or row1 == "1" or row1 == "2" or row1 == "3" or row1 == "4" or row1 == "5":
                                row1 = int(row1)
                                column1 = int(column1)
                                if check_move(game_board, row1, column1) == False:
                                    print("This moves is occupied !!")
                                    while True:
                                        print("Type 'Quit' to Quit")
                                        print("")
                                        print(
                                            "Player, please retype the column and row of your choice!")
                                        column1 = input(
                                            "Please type the column you want to put your marble : ")
                                        if column1 == "0" or column1 == "1" or column1 == "2" or column1 == "3" or column1 == "4" or column1 == "5":
                                            break
                                        elif column1 == "Quit":
                                            number == "Quit"
                                            break
                                        else:
                                            print(
                                                "Error! Please type a number between 0 to 5 inclusive")
                                    continue
                                else:
                                    pass
                                game_board = apply_move(
                                    game_board, 1, row1, column1, 0)
                                display_board(game_board)
                                check_victory(game_board, 1, 0)
                                if check_victory(game_board, 1, 0) == 1:
                                    print("Player Wins")
                                    break
                                elif check_victory(game_board, 1, 0) == 2:
                                    print("Computer Wins")
                                    break
                                elif check_victory(game_board, 1, 0) == 3:
                                    print("Draw! No player wins the game")
                                    break
                                while column1 != "Quit":
                                    print("Type 'Quit' to quit")
                                    print("")
                                    rot1 = input(
                                        "Player, please enter the rotation you want to apply : ")
                                    if rot1 == "1" or rot1 == "2" or rot1 == "3" or rot1 == "4" or rot1 == "5" or rot1 == "6" or rot1 == "7" or rot1 == "8":
                                        rot1 = int(rot1)
                                        game_board = apply_move(
                                            game_board, 1, row1, column1, rot1)
                                        break
                                    elif rot1 == "Quit":
                                        break
                                    else:
                                        print(
                                            "Error! Please type a number from 1 to 8 inclusive")
                                if rot1 == "Quit":
                                    pass
                                else:
                                    display_board(game_board)
                                    if check_victory(game_board, 1, rot1) == 1:
                                        print("Player wins")
                                        break
                                    elif check_victory(game_board, 1, rot1) == 2:
                                        print("Computer wins")
                                        break
                                    elif check_victory(game_board, 1, rot1) == 3:
                                        print("Draw! No player wins the game")
                                        break
                                break
                            elif row1 == "Quit":
                                number == "Quit"
                                break
                            else:
                                print(
                                    "Error! Please type a number between 0 to 5 inclusive")
                        if column1 == "Quit" or row1 == "Quit" or rot1 == "Quit":
                            break
                        if check_victory(game_board, 1, rot1) == 1:
                            break
                        if check_victory(game_board, 1, rot1) == 2:
                            break
                        print("Computer moves second! Computer is 2.")
                        print("")
                        print("This is the board before rotation")
                        row2, col2, rot2 = computer_move(game_board, 2, level)
                        game_board = apply_move(game_board, 2, row2, col2, 0)
                        display_board(game_board)
                        if check_victory(game_board, 2, 0) == 1:
                            print("Player wins")
                            break
                        elif check_victory(game_board, 2, 0) == 2:
                            print("Computer wins")
                            break
                        elif check_victory(game_board, 2, 0) == 3:
                            print("Draw! No player win the game")
                            break
                        print("")
                        print("This is the board after rotation")
                        game_board = apply_move(
                            game_board, 2, row2, col2, rot2)
                        display_board(game_board)
                        print("Computer moves is column", col2,
                              "row", row2, "and rotation", rot2)
                        check_victory(game_board, 2, rot1)
                        if check_victory(game_board, 2, rot2) == 1:
                            print("Player wins")
                            break
                        elif check_victory(game_board, 2, rot2) == 2:
                            print("Computer wins")
                            break
                        elif check_victory(game_board, 2, rot2) == 3:
                            print("Draw! No player win the game")
                            break
                    break
                elif turn == "2":
                    while True:
                        print("Computer moves first! Computer is 1.\n")
                        print("This is the board before rotation")
                        row1, col1, rot1 = computer_move(game_board, 1, level)
                        game_board = apply_move(game_board, 1, row1, col1, 0)
                        display_board(game_board)
                        if check_victory(game_board, 2, 0) == 1:
                            print("Computer wins")
                            break
                        elif check_victory(game_board, 2, 0) == 2:
                            print("Player wins")
                            break
                        elif check_victory(game_board, 2, 0) == 3:
                            print("Draw! No player win the game")
                            break
                        print("")
                        print("This is the board after rotation")
                        game_board = apply_move(
                            game_board, 1, row1, col1, rot1)
                        display_board(game_board)
                        print("Computer moves is column", col1,
                              "row", row1, "and rotation", rot1)
                        print("Player turn! Please indicate your movement.")
                        check_victory(game_board, 1, rot1)
                        if check_victory(game_board, 1, rot1) == 1:
                            print("Computer wins")
                            break
                        elif check_victory(game_board, 1, rot1) == 2:
                            print("Player wins")
                            break
                        elif check_victory(game_board, 1, rot1) == 3:
                            print("Draw! No winner")
                            break
                        while True:
                            print("Type 'Quit' to Quit")
                            print("")
                            column2 = input(
                                "Player, please type the column you want to put your marble : ")
                            if column2 == "0" or column2 == "1" or column2 == "2" or column2 == "3" or column2 == "4" or column2 == "5":
                                break
                            elif column2 == "Quit":
                                number == "Quit"
                                break
                            else:
                                print(
                                    "Error! Please type a number between 0 to 5 inclusive")
                        while rot1 != "Quit" and column2 != "Quit" and rot1 != "Quit":
                            print("Type 'Quit' to Quit")
                            print("")
                            row2 = input(
                                "Player, please type the row you want to put your marble : ")
                            if row2 == "0" or row2 == "1" or row2 == "2" or row2 == "3" or row2 == "4" or row2 == "5":
                                row2 = int(row2)
                                column2 = int(column2)
                                if check_move(game_board, row2, column2) == False:
                                    print("This moves is occupied !!")
                                    print(
                                        "Player, please retype the column and row of your choice!")
                                    while True:
                                        print("Type 'Quit' to Quit")
                                        print("")
                                        column2 = input(
                                            "Please type the column you want to put your marble : ")
                                        if column2 == "0" or column2 == "1" or column2 == "2" or column2 == "3" or column2 == "4" or column2 == "5":
                                            break
                                        elif column2 == "Quit":
                                            number == "Quit"
                                            break
                                        else:
                                            print(
                                                "Error! Please type a number between 0 to 5 inclusive")
                                    continue
                                else:
                                    pass
                                game_board = apply_move(
                                    game_board, 2, row2, column2, 0)
                                display_board(game_board)
                                if check_victory(game_board, 2, 0) == 1:
                                    print("Computer Wins")
                                    break
                                elif check_victory(game_board, 2, 0) == 2:
                                    print("Player Wins")
                                    break
                                elif check_victory(game_board, 2, 0) == 3:
                                    print("Draw! No player wins the game")
                                    break
                                while column2 != "Quit" and row2 != "Quit":
                                    print("Type 'Quit' to Quit")
                                    print("")
                                    rot2 = input(
                                        "Player, please enter the rotation you want to apply : ")
                                    if rot2 == "1" or rot2 == "2" or rot2 == "3" or rot2 == "4" or rot2 == "5" or rot2 == "6" or rot2 == "7" or rot2 == "8":
                                        rot2 = int(rot2)
                                        game_board = apply_move(
                                            game_board, 2, row2, column2, rot2)
                                        break
                                    elif rot2 == "Quit":
                                        break
                                    else:
                                        print(
                                            "Error! Please type a number from 1 to 8 inclusive")
                                if rot2 == "Quit":
                                    pass
                                else:
                                    display_board(game_board)
                                    if check_victory(game_board, 2, rot2) == 1:
                                        print("Computer Wins")
                                        break
                                    elif check_victory(game_board, 2, rot2) == 2:
                                        print("Player Wins")
                                        break
                                    elif check_victory(game_board, 2, rot2) == 3:
                                        print("Draw! No player wins the game")
                                        break
                                break
                            elif row2 == "Quit":
                                number == "Quit"
                                break
                            else:
                                print(
                                    "Error! Please type a number between 0 to 5 inclusive")
                        if column2 == "Quit" or row2 == "Quit" or rot2 == "Quit":
                            break
                        elif check_victory(game_board, 1, 0) == 1:
                            break
                        elif check_victory(game_board, 1, 0) == 2:
                            break
                        elif check_victory(game_board, 1, 0) == 3:
                            break
                        elif check_victory(game_board, 1, rot1) == 1:
                            break
                        elif check_victory(game_board, 1, rot1) == 2:
                            break
                        elif check_victory(game_board, 1, rot1) == 3:
                            break
                        elif check_victory(game_board, 2, 0) == 1:
                            break
                        elif check_victory(game_board, 2, 0) == 2:
                            break
                        elif check_victory(game_board, 2, 0) == 3:
                            break
                        elif check_victory(game_board, 2, rot2) == 1:
                            break
                        elif check_victory(game_board, 2, rot2) == 2:
                            break
                        elif check_victory(game_board, 2, rot2) == 3:
                            break
                        else:
                            continue
                    break
                elif turn == "Quit":
                    break
                else:
                    print("Error! Please type between 1, 2, or 'Quit'")
            break
        elif number == "3":
            display_board(game_board)
            while True:
                print("Player 1 turn! Please indicate your movement.")
                while True:
                    print("Type 'Quit' to Quit")
                    print("")
                    column1 = input(
                        "Player 1, please type the column you want to put your marble : ")
                    if column1 == "0" or column1 == "1" or column1 == "2" or column1 == "3" or column1 == "4" or column1 == "5":
                        break
                    elif column1 == "Quit":
                        number == "Quit"
                        break
                    else:
                        print("Error! Please type a number between 0 to 5 inclusive")
                if number == "Quit":
                    break
                while column1 != "Quit":
                    print("Type 'Quit' to Quit")
                    print("")
                    row1 = input(
                        "Player 1, please type the row you want to put your marble : ")
                    if row1 == "0" or row1 == "1" or row1 == "2" or row1 == "3" or row1 == "4" or row1 == "5":
                        row1 = int(row1)
                        column1 = int(column1)
                        if check_move(game_board, row1, column1) == False:
                            print("This moves is occupied !!")
                            while True:
                                print("Type 'Quit' to Quit")
                                print(
                                    "Player 1, please retype the column and row of your choice!")
                                print("")
                                column1 = input(
                                    "Please type the column you want to put your marble : ")
                                if column1 == "0" or column1 == "1" or column1 == "2" or column1 == "3" or column1 == "4" or column1 == "5":
                                    break
                                elif column1 == "Quit":
                                    number == "Quit"
                                    break
                                else:
                                    print(
                                        "Error! Please type a number between 0 to 5 inclusive")
                            continue
                        else:
                            pass
                        game_board = apply_move(
                            game_board, 1, row1, column1, 0)
                        display_board(game_board)
                        check_victory(game_board, 1, 0)
                        if check_victory(game_board, 1, 0) == 1:
                            print("Player 1 Wins")
                            break
                        elif check_victory(game_board, 1, 0) == 2:
                            print("Player 2 Wins")
                            break
                        elif check_victory(game_board, 1, 0) == 3:
                            print("Draw! No player wins the game")
                            break
                        while column1 != "Quit":
                            print("Type 'Quit' to quit")
                            print("")
                            rot1 = input(
                                "Player 1, please enter the rotation you want to apply : ")
                            if rot1 == "1" or rot1 == "2" or rot1 == "3" or rot1 == "4" or rot1 == "5" or rot1 == "6" or rot1 == "7" or rot1 == "8":
                                rot1 = int(rot1)
                                game_board = apply_move(
                                    game_board, 1, row1, column1, rot1)
                                break
                            elif rot1 == "Quit":
                                break
                            else:
                                print(
                                    "Error! Please type a number from 1 to 8 inclusive")
                        if rot1 == "Quit":
                            pass
                        else:
                            display_board(game_board)
                            if check_victory(game_board, 1, rot1) == 1:
                                print("Player 1 Wins")
                                break
                            elif check_victory(game_board, 1, rot1) == 2:
                                print("Player 2 Wins")
                                break
                            elif check_victory(game_board, 1, rot1) == 3:
                                print("Draw! No player wins the game")
                                break
                        break
                    elif row1 == "Quit":
                        number == "Quit"
                        break
                    else:
                        print("Error! Please type a number between 0 to 5 inclusive")
                if column1 == "Quit" or row1 == "Quit" or rot1 == "Quit":
                    break
                print("Player 2 turn! Please indicate your movement.")
                while column1 != "Quit" and row1 != "Quit":
                    print("Type 'Quit' to Quit")
                    print("")
                    column2 = input(
                        "Player 2, please type the column you want to put your marble : ")
                    if column2 == "0" or column2 == "1" or column2 == "2" or column2 == "3" or column2 == "4" or column2 == "5":
                        break
                    elif column2 == "Quit":
                        number == "Quit"
                        break
                    else:
                        print("Error! Please type a number between 0 to 5 inclusive")
                while rot1 != "Quit" and column1 != "Quit" and row1 != "Quit" and column2 != "Quit" and rot1 != "Quit":
                    print("Type 'Quit' to Quit")
                    print("")
                    row2 = input(
                        "Player 2, please type the row you want to put your marble : ")
                    if row2 == "0" or row2 == "1" or row2 == "2" or row2 == "3" or row2 == "4" or row2 == "5":
                        row2 = int(row2)
                        column2 = int(column2)
                        if check_move(game_board, row2, column2) == False:
                            print("This moves is occupied !!")
                            print(
                                "Player 2, please retype the column and row of your choice!")
                            while column1 != "Quit" and row1 != "Quit":
                                print("Type 'Quit' to Quit")
                                print("")
                                column2 = input(
                                    "Please type the column you want to put your marble : ")
                                if column2 == "0" or column2 == "1" or column2 == "2" or column2 == "3" or column2 == "4" or column2 == "5":
                                    break
                                elif column2 == "Quit":
                                    number == "Quit"
                                    break
                                else:
                                    print(
                                        "Error! Please type a number between 0 to 5 inclusive")
                            continue
                        else:
                            pass
                        game_board = apply_move(
                            game_board, 2, row2, column2, 0)
                        display_board(game_board)
                        if check_victory(game_board, 2, 0) == 1:
                            print("Player 1 Wins")
                            break
                        elif check_victory(game_board, 2, 0) == 2:
                            print("Player 2 Wins")
                            break
                        elif check_victory(game_board, 2, 0) == 3:
                            print("Draw! No player wins the game")
                            break
                        while column1 != "Quit" and row1 != "Quit" and column2 != "Quit":
                            print("Type 'Quit' to Quit")
                            print("")
                            rot2 = input(
                                "Player 2, please enter the rotation you want to apply : ")
                            if rot2 == "1" or rot2 == "2" or rot2 == "3" or rot2 == "4" or rot2 == "5" or rot2 == "6" or rot2 == "7" or rot2 == "8":
                                rot2 = int(rot2)
                                game_board = apply_move(
                                    game_board, 2, row2, column2, rot2)
                                break
                            elif rot2 == "Quit":
                                break
                            else:
                                print(
                                    "Error! Please type a number from 1 to 8 inclusive")
                        if rot2 == "Quit":
                            pass
                        else:
                            display_board(game_board)
                            if check_victory(game_board, 2, rot2) == 1:
                                print("Player 1 Wins")
                                break
                            elif check_victory(game_board, 2, rot2) == 2:
                                print("Player 2 Wins")
                                break
                            elif check_victory(game_board, 2, rot2) == 3:
                                print("Draw! No player wins the game")
                                break
                        break
                    elif row2 == "Quit":
                        number == "Quit"
                        break
                    else:
                        print("Error! Please type a number between 0 to 5 inclusive")
                if column2 == "Quit" or row2 == "Quit" or rot2 == "Quit":
                    break
                elif check_victory(game_board, 1, 0) == 1:
                    break
                elif check_victory(game_board, 1, 0) == 2:
                    break
                elif check_victory(game_board, 1, 0) == 3:
                    break
                elif check_victory(game_board, 1, rot1) == 1:
                    break
                elif check_victory(game_board, 1, rot1) == 2:
                    break
                elif check_victory(game_board, 1, rot1) == 3:
                    break
                elif check_victory(game_board, 2, 0) == 1:
                    break
                elif check_victory(game_board, 2, 0) == 2:
                    break
                elif check_victory(game_board, 2, 0) == 3:
                    break
                elif check_victory(game_board, 2, rot2) == 1:
                    break
                elif check_victory(game_board, 2, rot2) == 2:
                    break
                elif check_victory(game_board, 2, rot2) == 3:
                    break
                else:
                    continue
            number == "Quit"
            break
        elif number == "Quit":
            break
        else:
            print("Error! Please type the number between 1, 2, or 3 or 'Quit' ")


if __name__ == "__main__":
    menu()
