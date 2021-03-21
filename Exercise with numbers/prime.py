#is the number a prime?
#https://edabit.com/challenge/EcBpRwgYsbmEWXKB9

x = int(input("Is the number prime? "))

def prime_foo(x):
    prime = True
    for i in range(2,x-1):
        if x % i == 0:
            prime = False
            break
    return prime


print(prime_foo(x))
