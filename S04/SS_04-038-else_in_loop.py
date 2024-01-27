numbers = [1, 5, 11, 13]

for number in numbers:
    if number % 2 == 0:
        print("We got even numbers")
        break
else:
    print("We dont have any Even numbers")