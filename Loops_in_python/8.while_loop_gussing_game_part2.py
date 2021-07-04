import random
n = 20
to_be_gussed = int(n * random.random()) + 1
guess = 0
while guess != to_be_gussed:
    guess = int(input("New number: "))
    if guess > 0:
        if guess > to_be_gussed:
            print("Number too large")
        elif guess < to_be_gussed:
            print("Number too small")
    else:
        print("Sorry that you're giving up!")
        break
else:
    print("Congratulation. You made it!")