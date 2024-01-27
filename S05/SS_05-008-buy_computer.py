available_parts = ['Computer', 'Monitor', 'Keyboard', 'Mouse', 'Mouse Pad', 'HDMI', 'DVD DRIVE']
valid_choices = [str(i) for i in range(1, len(available_parts) + 1)]
current_choice = "-"
computer_parts = []  # create an empty list

while current_choice != '0':
    if current_choice in valid_choices:

        index = int(current_choice) - 1
        chosen_part = available_parts[index]
        if chosen_part in computer_parts:
            print("Removing {}".format(current_choice))
            computer_parts.remove(chosen_part)
        else:
            print("Adding {}".format(current_choice))
            computer_parts.append(chosen_part)
        print(computer_parts)
    else:
        print("Please add options from the list below:")
        for number, parts in enumerate(available_parts):
            print("{0}: {1}".format(number + 1, parts))
        print("0: to Finish")

    current_choice = input()

print(computer_parts)