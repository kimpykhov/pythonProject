count = 558
running = True

while running:
    guess = int(input("check: "))

    if guess == count:
        print('awesome')
        runnung = False
    elif guess < count:
        print("fuck less")
    else:
        print("fuck more")