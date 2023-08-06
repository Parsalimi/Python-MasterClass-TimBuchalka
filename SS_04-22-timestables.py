line = ""
space = " "
for i in range(1, 11):
    line = line + "\t" +str(i)
print(line)
line = ""
for i in range(1, 11):
    for j in range(1,11):
        line = line + "\t" + str(i*j)
    print(str(i) + line)
    line = ""