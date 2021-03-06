#https://edabit.com/challenge/hQRuQguN4bKyM2gik

x = int(input("First number: "))
y = int(input("Second number: "))

def foo(a,b):
    max_number = max(a,b)
    min_number = min(a,b)
    i = 0
    while min_number > 0:
        if max_number % min_number == 0:
            i += 1
        max_number -= 1
        min_number -= 1
    return i

print(foo(x,y))
