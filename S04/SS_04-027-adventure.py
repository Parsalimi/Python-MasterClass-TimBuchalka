availabe_exits = ["north", "west", "east", "south"]

choosen_exit = ""
while choosen_exit not in availabe_exits:
    choosen_exit = input("Please choose a direction: ")
    if choosen_exit.casefold() == "quit":
        print("Game Over!")
        break

print("arent you glad you got out of there")