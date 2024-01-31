data = [4, 5, 104, 105, 110, 120, 130, 150,
        160, 170, 183,185, 187,188, 191, 350, 360]

# havasemon bashe estefade az del size object ma ro be ham mirize
# del data[0:2]
# print(data)
#
# del data[14:]
# print(data)

min_valid = 100
max_valid = 200

start = 0
for index, value in enumerate(data):
        if value >= min_valid:
                start = index
                break
stop = 0
for index in range(len(data) - 1, -1, -1):
        if data[index] <= max_valid:
                stop = index + 1
                break

print(data[start:stop])
