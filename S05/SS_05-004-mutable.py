computer_parts = ["computer",
                  "monitor",
                  "keyboard",
                  "mouse",
                  "mouse pad"
                  ]

another_list = computer_parts
print(id(computer_parts))
print(id(another_list))

computer_parts += ["cookies"]
print(id(computer_parts))
print(another_list)

a = b = c = d = e = f = another_list
print(id(a))