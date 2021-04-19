def score(dice):
    final_score = 0
    for i in range(1,7):
        if dice.count(i) == 3:
            if i == 1:
                final_score += 1000
            elif i == 2:
                final_score += 200
            elif i == 3:
                final_score += 300
            elif i == 4:
                final_score += 400
            elif i == 5:
                final_score += 500
            elif i == 6:
                final_score += 600
            dice.remove(i)
            dice.remove(i)
            dice.remove(i)
        elif dice.count(i) == 1:
            if i == 1:
                final_score += 100
            elif i == 5:
                final_score += 50
            dice.remove(i)
    return final_score
