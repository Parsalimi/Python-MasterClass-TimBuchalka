shopping_list = ["milk","pasta","eggs","spam","rice","bread"]

item_to_find = "spams"
found_at = None

# for index in range(6):
# for index in range(len(shopping_list)):
#     if shopping_list[index] == item_to_find:
#         found_at = index
#         break

if item_to_find in shopping_list:
    found_at = shopping_list.index(item_to_find)

if found_at is not None:
    print("Item found at position {}".format(found_at))
else:
    print("Didn't find {}".format(item_to_find))