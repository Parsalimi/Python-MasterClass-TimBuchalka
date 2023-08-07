for i in range(0,100):
    if i > 0 and i % 11 == 0:
        print("the number that we're looking for is {}".format(i))
        break
    else:
        print("i is now {}".format(i))