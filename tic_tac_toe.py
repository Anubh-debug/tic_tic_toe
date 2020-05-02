import random

def game(player):
    i = 0
    position_list = []
    game_list_one = [0, 1, 2]
    game_list_two = [3, 4, 5]
    game_list_three = [6, 7, 8]
    print("ready players and the player " + str(player) + " will start first.")
    print(game_list_one)
    print(game_list_two)
    print(game_list_three)
    print("enter position in which you want to insert")
    while i < 9:
        if player == 1:
            repeat = False
            position = int(input())
            if position not in position_list:
                position_list.append(position)
            else:
                repeat = True
                print("enter a valid place")
                i -= 1
            if position < 3 and repeat == False:
                game_list_one[position] = "X"
            elif position > 2 and position < 6 and repeat == False:
                position = position % 3
                game_list_two[position] = "X"
            elif position > 5 and position < 9 and repeat == False:
                position = position % 3
                game_list_three[position] = "X"
            print(game_list_one)
            print(game_list_two)
            print(game_list_three)
            if game_list_one[0] == "X" and game_list_one[1] == "X" and game_list_one[2] == "X":
                print("player 1 is winner")
                break
            elif game_list_two[0] == "X" and game_list_two[1] == "X" and game_list_two[2] == "X":
                print("player 1 is winner")
                break
            elif game_list_three[0] == "X" and game_list_three[1] == "X" and game_list_three[2] == "X":
                print("player 1 is winner")
                break
            elif game_list_one[0] == "X" and game_list_two[0] == "X" and game_list_three[0] == "X":
                print("player 1 is winner")
                break
            elif game_list_one[1] == "X" and game_list_two[1] == "X" and game_list_three[1] == "X":
                print("player 1 is winner")
                break
            elif game_list_one[2] == "X" and game_list_two[2] == "X" and game_list_three[2] == "X":
                print("player 1 is winner")
                break
            elif game_list_one[0] == "X" and game_list_two[1] == "X" and game_list_three[2] == "X":
                print("player 1 is winner")
                break
            elif game_list_one[2] == "X" and game_list_two[1] == "X" and game_list_three[0] == "X":
                print("player 1 is winner")
                break
            if repeat == False:
                print("player 2 chance")
                player = 2
            else:
                print("enter your chance again")
                player = 1
        else:
            repeat = False
            position = int(input())
            if position not in position_list:
                position_list.append(position)
            else:
                repeat = True
                print("enter a valid place")
                i -= 1
            if position < 3 and repeat == False:
                game_list_one[position] = "O"
            elif position > 2 and position < 6 and repeat == False:
                position = position % 3
                game_list_two[position] = "O"
            elif position > 5 and position < 9 and repeat == False:
                position = position % 3
                game_list_three[position] = "O"
            print(game_list_one)
            print(game_list_two)
            print(game_list_three)
            if game_list_one[0] == "O" and game_list_one[1] == "O" and game_list_one[2] == "O":
                print("player 2 is winner")
                break
            elif game_list_two[0] == "O" and game_list_two[1] == "O" and game_list_two[2] == "O":
                print("player 2 is winner")
                break
            elif game_list_three[0] == "O" and game_list_three[1] == "O" and game_list_three[2] == "O":
                print("player 2 is winner")
                break
            elif game_list_one[0] == "O" and game_list_two[0] == "O" and game_list_three[0] == "O":
                print("player 2 is winner")
                break
            elif game_list_one[1] == "O" and game_list_two[1] == "O" and game_list_three[1] == "O":
                print("player 2 is winner")
                break
            elif game_list_one[2] == "O" and game_list_two[2] == "O" and game_list_three[2] == "O":
                print("player 2 is winner")
                break
            elif game_list_one[0] == "O" and game_list_two[1] == "O" and game_list_three[2] == "O":
                print("player 2 is winner")
                break
            elif game_list_one[2] == "O" and game_list_two[1] == "O" and game_list_three[0] == "O":
                print("player 2 is winner")
                break
            if repeat == False:
                print("player 1 chance")
                player = 1
            else:
                print("enter your chance again")
                player = 2
        i += 1
    print("Match draw. Play again to decide the winner.")

if __name__ == '__main__':
    print("------Welcome to tic tac toe------")
    print("------This game is for two people------")
    print("------Are you ready for toss------")
    print("yes/no")
    permit = input()
    if permit == "yes":
        toss = random.randrange(1, 3)
        if toss == 1:
            player = 1
            print("player 1 has won the toss.")
            print("player 1 will start first and play with X")
            print("player 2 will play with another symbol")
            game(player)
            print("$$$$$$$$$$Thanks for playing$$$$$$$$$$")
        else:
            player = 2
            print("player 2 has won the toss.")
            print("player 2 will start first and play with O")
            print("player 1 will play with another symbol")
            game(player)
            print("$$$$$$$$$$Thanks for playing$$$$$$$$$$")

    else:
        print("------please restart the program if you want to play------")

