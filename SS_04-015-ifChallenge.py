name = input("Please enter your name: ")
age = int(input("Please enter your age, {}: ".format(name)))
if 18 <= age < 31:
    print("Welcome to our holiday plan for this summer")
else:
    print("Thanks for choosing us for your dream holidays week but we have age restriction and you're not applied")