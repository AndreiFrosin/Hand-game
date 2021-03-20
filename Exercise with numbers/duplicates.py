def duplicate_count(text):
    counter1 = 0
    text= text.upper()
    for i in set(text):
        counter = text.count(i)
        if counter>1:
            counter1 +=1
            counter = 0
    return counter1
