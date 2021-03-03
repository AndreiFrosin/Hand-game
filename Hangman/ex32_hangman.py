#HANGMAN
#3 difficulty levels: 1-easy (<4 letters), 2-medium(4-6 letters), 3-hard(7+ letters)
#player has 6 guesses(head, body, 2 arms, 2 legs)
#

import random


run = True
easy = []
medium = []
hard = []

with open("hangman.txt","r") as file:
    all_text = file.read()
text = all_text.split()
for i in text:
    if len(i) < 4:
        easy.append(i)
    elif 3 < len(i) < 7:
        medium.append(i)
    else:
        hard.append(i)

print("""
You have 6 tries to find the word.
If you fail ... you die!
""")

def foo(lista):
    computer_choice = random.choice(lista)
    print(f"Word to guess has {len(computer_choice)} letters.")
    word_to_guess = ("-") * len(computer_choice)
    print(word_to_guess)
    guesses = 0


    while guesses < 6 or "-" not in word_to_guess :

        user_letter = input("Guess a letter: ")
        if user_letter in computer_choice:
            for i in range(len(computer_choice)):
                if computer_choice[i] == user_letter:
                    word_to_guess = word_to_guess[:i] + user_letter + word_to_guess[i+1:]
            if "-" not in word_to_guess:
                print("You win!")


        else:
            print("Wrong choice.")
            guesses += 1
            print(f"Number of tries left: {6 - guesses} \n")

            if guesses == 1:
                print('''
   +---+
   O   |
       |
       |
      ===''')
            if guesses == 2:
                print('''
    +---+
    O   |
    |   |
        |
       ===''')
            if guesses == 3:
                print('''
    +---+
    O   |
   /|   |
        |
       ===''')
            if guesses == 4:
                print('''
    +---+
    O   |
   /|\  |
        |
       ===''')
            if guesses == 5:
                print('''
    +---+
    O   |
   /|\  |
   /    |
       ===''')
            if guesses == 6:
                print('''
    +---+
    O   |
   /|\  |
   / \  |
       ===''')
                print("You lose!")
                print(f"The word to guess is : {computer_choice}")
        print(word_to_guess + "\n")

    return

while run:
#1-easy
    player_choice = int(input("Choose the difficulty (1-easy, 2-medium, 3-hard): "))
    print(" \n")
    if player_choice == 1:
        foo(easy)
    elif player_choice == 2:
        foo(medium)
    elif player_choice == 3:
        foo(hard)
    else:
        print("I don't understand your choice..")


    print("Do you want to continue? Y or N: ")
    continue_play = input("> ")
    if continue_play.upper() == "Y":
        pass
    elif continue_play.upper() == "N":
        run = False
    else:
        print("I don't understand that..")
