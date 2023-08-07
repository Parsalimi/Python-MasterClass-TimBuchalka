import random

highest = 1000
answer = random.randint(1, highest)
wining_status = False
round_played = 1
print(answer)

print("YOU ONLY HAVE 10 GUESS")
guess = int(input("1. Please guess a number between 1 and {}: ".format(highest)))

while not round_played > 9:
    if guess == 0:
        print("{}. QUITED!!!".format(round_played))
        break
    else:
        if guess == answer:
            print("You got it {}th time".format(round_played))
            break
        elif guess > answer:
            guess = int(input("{}. Please guess lower: ".format(round_played + 1)))
        else:
            guess = int(input("{}. Please guess higher: ".format(round_played + 1)))
    round_played += 1

print("You didn't guess it")