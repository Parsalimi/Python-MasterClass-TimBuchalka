shopping_list = ["milk","pasta","eggs","spam","rice","bread"]

# for item in shopping_list:
#     if item != "spam":
#         print("Buy " + item)
#
# for item in shopping_list:
#     if item == "spam":
#         continue
#
#     print("Buy " + item)


for item in shopping_list:
    if item == "spam":
        break

    print("Buy " + item)