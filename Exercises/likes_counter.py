def likes(names):
    if names == []:
        x = 'no one likes this'

    elif len(names) == 1:
        x = f'{names[0]} likes this'

    elif len(names) == 2:
        x = f'{names[0]} and {names[1]} like this'

    elif len(names) ==3:
        x = f'{names[0]}, {names[1]} and {names[2]} like this'

    else:
        y = len(names) - 2
        x = f'{names[0]}, {names[1]} and {y} others like this'

    return x
