number = "9,223;036 854,775;807"
separators = number[1::4]
print(separators)
print("-"*20)
separators = ""
for char in number:
    if not char.isnumeric():
        separators = separators + char

print(separators)