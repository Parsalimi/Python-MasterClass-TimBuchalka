panagram = """The quick brown 
foxs jumps\tover 
the lazy dog"""

words = panagram.split()
print(words)

numbers = "9,123,243,546,324,476"
words = numbers.split(",")
print(words)


generated_list = [
    '9', ' ',
    '2', '2', '3', ' ',
    '3', '7', '2', ' ',
    '0', '3', '6', ' ',
    '8', '5', '4', ' ',
    '7', '7', '5', ' ',
    '8', '0', '7'
]

values = "".join(generated_list)
print(values)


values_list = values.split()
print(values_list)