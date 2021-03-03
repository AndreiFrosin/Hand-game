from random import *

keep_playing = True
while keep_playing: 

    print('-'*10)
    player_choice = input("Choose [rock, papper, cissor]: ")
    basic_choice = ["rock", "papper", "cissor"]
    list_choice = randint(0,2)
    computer_choice = basic_choice[list_choice]

    win1= player_choice == "rock" and computer_choice == "cissor"
    win2= player_choice == "papper" and computer_choice == "rock"
    win3= player_choice == "cissor" and computer_choice == " papper"

    tie= player_choice == computer_choice

    if win1 or win2 or win3:
        print("You win!.")

    elif tie:
        print("Tie!")

    else:
        print("You lose.")

    print(f"Computer chose:{computer_choice}")

    player_choice_keep_playing= input("Keep playing? [y/n]")
    if player_choice_keep_playing == "y":
        pass
    else:
        keep_playing = False
