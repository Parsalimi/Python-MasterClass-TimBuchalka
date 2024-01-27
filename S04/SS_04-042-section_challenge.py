choice = "-"
while choice != "0":
    if choice in "12345":
        print("you chose {}".format(choice))
    else:
        print("Please Choose your options form the list below:")
        print("1.\tLearn Python")
        print("2.\tLearn Java")
        print("3.\tGo Swimming")
        print("5.\tGo to Bed")
        print("0.\tExit")

    choice = input()