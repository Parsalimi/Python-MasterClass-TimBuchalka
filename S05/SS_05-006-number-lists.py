empty_list = []
even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

numbers = even + odd

sorted_numbers1 = sorted(numbers)
print(numbers)
print(sorted_numbers1)
print(numbers.sort())
print(id(numbers))
print(id(sorted_numbers1))
print(id(numbers.sort()))

digits = list("431526978")
print(digits)
print(digits.sort())

more_list_numbers = list(numbers)
print(more_list_numbers)
# print(min(even))
# print(max(even))
# print(len(odd))
# print("mississippi".count("issi"))

# even.extend(odd)
# print(even)
#
# even.sort()
# print(even)
# another_list = even
# even.sort(reverse=True)
# print(even)
# print(another_list)

