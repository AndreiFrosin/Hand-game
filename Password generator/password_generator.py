import string, random


low_string = string.ascii_letters
medium_string = string.ascii_letters + string.digits
high_string = string.printable

def easy_pass(char):
    easy_pwd = random.sample(low_string,char)
    return "".join(easy_pwd)

def medium_pass(char):
    medium_pwd = random.sample(medium_string,char)
    return "".join(medium_pwd)

def high_pass(char):
    high_pwd = random.sample(high_string,char)
    return "".join(high_pwd)

user_difficulty = int(input("Choose the difficulty:\n 1-Easy \n 2-Medium \n 3-High \n >"))
user_char = int(input("Choose the number of characters: "))

if user_difficulty == 1:
    print("password: " + easy_pass(user_char))
elif user_difficulty == 2:
    print("password: " + medium_pass(user_char))
elif user_difficulty == 3:
    print("password: " + high_pass(user_char))
else:
    print("Wrong difficulty level.")
