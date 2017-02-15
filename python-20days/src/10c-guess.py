import random

n = random.randint(1, 30)

while True:
    x = input("please guess number between 1 and 30")
    g = int(x)
    
    if g == n:
        print("Correct!")
        break
    if g < n:
        print("too small")
    if g > n:
        print("too big") 