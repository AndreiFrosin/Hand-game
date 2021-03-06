#Can you spare a square?
#https://edabit.com/challenge/joCBaJztZrdxi9HjR

people = int(input("Number of people in the household: "))
tp = int(input("Number of rolls: "))

tp_dict = {"people": people, "tp": tp}

def tp_checker(dict):
    tp_people = dict.get("people") * 57
    days = dict.get("tp") * 500 // tp_people
    if days < 14:
        print(f"Your TP will only last {days} days, buy more!")
    else:
        print(f"Your TP will last {days} days, no need to panic!")

tp_checker(tp_dict)
