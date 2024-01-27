parrot = "Norwegian Blue"

letter = input("Please enter character: ")
if letter in parrot:
    print("There is {0} in {1}".format(letter, parrot))
else:
    print("There is not {0} in {1}".format(letter, parrot))