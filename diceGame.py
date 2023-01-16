"""
Name: Vadim Reger
Username: vreg113
Description of the program: this program is a game called Poaka for 2 players.
Each player takes turns at rolling the dice. At each turn, the player repeatedly rolling the dice. If the player gets 1
then he gets 0 for this turn. The game goes until one of the players reach needed points to win.
"""

import random


def main():
    player2_is_automated = True
    name_player1 = "Jack"
    name_player2 = "Computer"

    wins_player1 = 0
    wins_player2 = 0

    game_has_ended = False

    welcome_to_game(name_player1, name_player2)  # 1.

    while not game_has_ended:
        game_winner = play_one_game(name_player1, name_player2, player2_is_automated)

        if game_winner == 1:
            wins_player1 += 1
        else:
            wins_player2 += 1

        if not wants_to_play_again():  # 13.
            game_has_ended = True

    display_final_results(wins_player1, wins_player2, name_player1, name_player2)   # 14.

# ------------------------------------
# 1. welcome_to_game()
# This function print the name of the game, who made it and hwo is playing
# ------------------------------------


def welcome_to_game(player1, player2):
    number_of_stars = 42
    print("\n", "*" * number_of_stars, sep="")
    print("     Welcome to POAKA by vreg113")
    print(" " * 4, player1, "versus", player2)
    print("*" * number_of_stars, "\n", sep="")

# ------------------------------------
# 2. get_starting_player_number()
# Function randomly choosing the first player
# ------------------------------------


def get_starting_player_number():
    random_number = random.randrange(1, 3)
    return random_number

# ------------------------------------
# 3. get_player_name()
# Function getting the name of the player
# ------------------------------------


def get_player_name(player_number, name_player1, name_player2):
    if player_number == 1:
        return name_player1
    else:
        return name_player2

# ------------------------------------
# 4. get_player_score()
# Function that get the player score
# ------------------------------------


def get_player_score(player_number, score_player1, score_player2):
    if player_number == 1:
        return score_player1
    else:
        return score_player2
# ------------------------------------
# 5. get_other_player_name_and_score()
# Function that return the player's score
# ------------------------------------


def get_other_player_name_and_score(player_number, name_player1, name_player2, score_player1, score_player2):
    if player_number == 1:
        string = name_player2 + "'s score: " + str(score_player2)
    else:
        string = name_player1 + "'s score: " + str(score_player1)
    return string

# ------------------------------------
# 6. display_player_turn_info()
# Function display turn info
# ------------------------------------


def display_player_turn_info(player_name, player_score, other_player_info):
    number_of_stars = 42
    print("\n", "*" * number_of_stars, sep="")
    print(str(player_name) + "'s turn (score: " + str(player_score) + ") (" + str(other_player_info) + ")" + "\n")


# ------------------------------------
# 7. dice_roll_contains_a_one()
# Function check whether the dice roll have 0 or not
# ------------------------------------


def dice_rolls_contains_a_one(dice_string):
    find_index_of_1 = dice_string.find("1")
    if find_index_of_1 == -1:
        return False
    else:
        return True

# ------------------------------------
# 8. get_sum_of_dice()
# Function finding the sum of the dice
# ------------------------------------


def get_sum_of_dice(dice_string):
    counter = 0
    total = 0
    while counter != len(dice_string):
        total = total + int(dice_string[counter])
        counter = counter + 1
    return total

# ------------------------------------
# 9. game_has_been_won()
# Function check whether the game was won or not
# ------------------------------------


def game_has_been_won(player1_score, player2_score, game_score):
    if (player1_score >= game_score) or (player2_score >= game_score):
        return True
    else:
        return False

# ------------------------------------
# 10. get_other_player_number()
# Function getting other player number
# ------------------------------------


def get_other_player_number(current_player_number):
    if current_player_number == 1:
        return 2
    else:
        return 1

# ------------------------------------
# 11. get_winner_number()
# Function get the winner player number
# ------------------------------------


def get_winner_number(score_player1, score_player2):
    if score_player1 > score_player2:
        return 1
    else:
        return 2

# ------------------------------------
# 12. congratulate_winner()
# Function that display congratulations to the winner
# ------------------------------------


def congratulate_winner(winner_name):
    number_of_stars = 42
    print("\n", "*" * number_of_stars, sep="")
    print("     Well done " + str(winner_name) + "! You have won!")
    print("*" * number_of_stars, "\n", sep="")

# ------------------------------------
# 13. wants_to_play_again()
# Function ask whether you want to play again or not
# ------------------------------------


def wants_to_play_again():
    user_choice = input("     Would you like to play again (y or n):  ")
    if user_choice == "y":
        return True
    else:
        return False

# ------------------------------------
# 14. display_final_results()
# Function display the final result
# ------------------------------------


def display_final_results(wins_player1, wins_player2, name_player1, name_player2):
    number_of_stars = 42
    print("\n\n", "*" * number_of_stars, sep="")
    if wins_player1 == wins_player2:
        print("     Everyone is a winner!  -", wins_player1)
    elif wins_player1 > wins_player2:
        print("     The winner: " + name_player1.upper() + " - " + str(wins_player1))
        print("     Runner up:  " + name_player2 + " - " + str(wins_player2))
    else:
        print("     The winner: " + name_player2.upper() + " - " + str(wins_player2))
        print("     Runner up:  " + name_player1 + " - " + str(wins_player1))
    print("*" * number_of_stars, "\n\n", sep="")


# ------------------------------------
# 15. computer_wants_roll_again()
# Function that making decisions for player 2 (Computer)
# ------------------------------------


def computer_wants_roll_again(dice_string_so_far, score_player1, score_player2, points_needed_to_win):
    # Finding current score
    current_score = score_player2 + get_sum_of_dice(dice_string_so_far)
    # If computer's current score is more than points needed to win, computer stop rolling the dice
    if current_score >= points_needed_to_win:
        return False
    # If player 1 is very close to win (need less than 7 points) than computer trying to win the game on this turn
    if (points_needed_to_win - score_player1) <= 7:
        return True
    # If computer is very close to win the round, computer will try to win on this turn
    if (points_needed_to_win - current_score) <= 6:
        return True
    # If all of the above choices are not executing, computer will roll the dice 4 times
    if len(dice_string_so_far) < 4:
        return True
    # If nothing from the above work, then computer will stop after rolling the dice 4 times.
    return False


def get_string_of_dice_rolls():
    dice_string = ""
    user_input = input("   ")
    while user_input == "":
        dice_roll = str(random.randrange(1, 7))
        dice_roll_display = "    Your dice: " + dice_roll + " "
        dice_string = dice_string + dice_roll
        if dice_roll == "1":
            print(dice_roll_display, "Ooops! You rolled a one!")
            return dice_string
        user_input = input(dice_roll_display)
    return dice_string


def play_one_game(name_player1, name_player2, player2_is_automated):
    points_needed_to_win = 30

    score_player1 = 0
    score_player2 = 0

    winnner_number = 0
    current_score = 0
    game_has_ended = False

    current_player_number = get_starting_player_number()  # 2.

    while not game_has_ended:
        current_player_name = get_player_name(current_player_number, name_player1, name_player2)  # 3.
        current_player_score = get_player_score(current_player_number, score_player1, score_player2)  # 4.
        other_player_info = get_other_player_name_and_score(current_player_number, name_player1, name_player2, score_player1, score_player2)  # 5.
        display_player_turn_info(current_player_name, current_player_score, other_player_info)  # 6.

        if player2_is_automated and current_player_number == 2:
            turn_score = computer_has_a_turn(current_player_name, score_player1, score_player2, points_needed_to_win)
        else:
            turn_score = have_a_turn(current_player_name)

        if current_player_number == 1:
            score_player1 = score_player1 + turn_score
        else:
            score_player2 = score_player2 + turn_score

        if game_has_been_won(score_player1, score_player2, points_needed_to_win):  # 9.
            game_has_ended = True
        else:
            current_player_number = get_other_player_number(current_player_number)  # 10.


    winnning_player_number = get_winner_number(score_player1, score_player2)  # 11.
    name_winner = get_player_name(winnning_player_number, name_player1, name_player2)
    congratulate_winner(name_winner)  # 12.

    return winnning_player_number


def computer_has_a_turn(current_player_name, score_player1, score_player2, points_needed_to_win):
    score_this_turn = 0
    print(current_player_name + ", keep on pressing ENTER to continue \n         rolling the dice (anything else\n         to end your turn)")
    string_of_dice = ""
    wants_to_roll_again = True
    while wants_to_roll_again:
        dice_roll = str(random.randrange(1, 7))

        dice_roll_display = "    Your dice: " + dice_roll + " "
        print(dice_roll_display)
        string_of_dice = string_of_dice + dice_roll
        if dice_roll == "1":
            print("    Ooops! You rolled a one!")
            return 0

        wants_to_roll_again = computer_wants_roll_again(string_of_dice, score_player1, score_player2,
                                                   points_needed_to_win)  # 15.
    score_this_turn = get_sum_of_dice(string_of_dice)  # 8.
    return score_this_turn


def have_a_turn(player_name):
    score_this_turn = 0
    print(player_name + ", keep on pressing ENTER to continue \n         rolling the dice (anything else\n         to end your turn)")
    string_of_dice = get_string_of_dice_rolls()

    if dice_rolls_contains_a_one(string_of_dice):  # 7.
        return 0

    score_this_turn = get_sum_of_dice(string_of_dice)  # 8.
    return score_this_turn


main()
