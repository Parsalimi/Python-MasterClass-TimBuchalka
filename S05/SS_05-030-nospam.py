menu = [
    ["egg", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "sausage", "spam", "bacon", "spam", "tomato", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
]

# for meal in menu:
#     if "spam" in meal:
#         for index, food in enumerate(meal):
#             if food == "spam":
#                 meal.pop(index)
#         print(meal)
#     else:
#         print(meal)


# for meal in menu:
#     top_index = len(meal) - 1
#     for index, food in enumerate(reversed(meal)):
#         if food == "spam":
#             del meal[top_index - index]
#     print(meal)

# for meal in menu:
#     for index in range(len(meal) -1, -1, -1):
#         if meal[index] == "spam":
#             del meal[index]
#     print(meal)

for meal in menu:
    for food in meal:
        if food != "spam":
            print(food, end=" ")
    print()