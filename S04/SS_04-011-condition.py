age = int(input("Please enter your age? "))

# if age >= 18 and age <= 70:
#     print("You've to WORK!")

if 18 <= age <= 70:
    print("You've to WORK!")
else:
    print("Enjoy your free time!")

print("-"*25)

if age < 18 or age > 70:
    print("Enjoy your free time!")
else:
    print("You've to WORK!")

print("-"*25)

if age in range(18, 71):
    print("You've to WORK!")

else:
    print("Enjoy your free time!")