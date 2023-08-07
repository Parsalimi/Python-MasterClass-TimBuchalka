import random

highest = 50
answer = random.randint(1, highest)
wining_status = False
round_played = 0
print(answer) # TODO: remove after testing

guess = int(input("Please guess a number between 1 and {}: ".format(highest)))
while not wining_status:
    round_played += 1
    if guess == 0:
        print("QUITED!!!")
        wining_status = True
    else:
        if guess == answer:
            print("You got it {}th time".format(round_played)) #TODO: First time
            wining_status = True
        elif guess > answer:
            guess = int(input("Please guess lower: "))
        else:
            guess = int(input("Please guess higher: "))

