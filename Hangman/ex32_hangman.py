#HANGMAN
#3 difficulty levels: 1-easy (<4 letters), 2-medium(4-6 letters), 3-hard(7+ letters)
#player has 6 guesses(head, body, 2 arms, 2 legs)
#

import random


run = True
easy = []
medium = []
hard = []

#create 3 different lists based on the word no. of characters
with open("hangman.txt","r") as file:
    all_text = file.read()
text = all_text.split()
for i in text:
    if len(i) < 4:
        #if the word has less then 4 characters, it will be appended to the easy list
        easy.append(i)
    elif 3 < len(i) < 7:
        #words with 4 up to 6 chars will be put in medium list
        medium.append(i)
    else:
        #words with more then 7 chars will be put in hard list
        hard.append(i)

print("""
You have 6 tries to find the word.
If you fail ... you die!
""")

#graphical hang
def print_hang(x):
    if x == 1:
        print('''
  +---+
  O   |
      |
      |
 ===''')
    if x == 2:
        print('''
  +---+
  O   |
  |   |
      |
 ===''')
    if x == 3:
        print('''
  +---+
  O   |
 /|   |
      |
 ===''')
    if x == 4:
        print('''
  +---+
  O   |
 /|\  |
      |
 ===''')
    if x == 5:
        print('''
  +---+
  O   |
 /|\  |
 /    |
 ===''')
    if x == 6:
        print('''
  +---+
  O   |
 /|\  |
 / \  |
===''')


#the function usses a list chosen by the difficulty level
def foo(lista):
    #the computer chooses a random word from the list
    computer_choice = random.choice(lista)
    #we print the number of chars and a visual hint of the hidden word
    print(f"Word to guess has {len(computer_choice)} letters.")
    word_to_guess = ("-") * len(computer_choice)
    print(word_to_guess)
    guesses = 0


    while guesses < 6 or "-" not in word_to_guess :
        #the user start guessing the letters
        #if the letter is correct, we update "word_to_guess"
        user_letter = input("Guess a letter: ")
        if user_letter in computer_choice:
            for i in range(len(computer_choice)):
                if computer_choice[i] == user_letter:
                    word_to_guess = word_to_guess[:i] + user_letter + word_to_guess[i+1:]
            if "-" not in word_to_guess:
                print("You win!")

        #if the guess is wrong, we show a graphical hang
        else:
            print("Wrong choice.")
            guesses += 1
            print(f"Number of tries left: {6 - guesses} \n")
            print_hang(guesses)
            if guesses == 6:
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
