low = 1
high = 1000
# mige ke ba estefade az binary search mishe az bein adad 0 ta 1023 ro hadaksar dar 10 marhale peyda kard
print("Please think of a number between {} and {}".format(low, high))
round_played = 0

guess = 1
while low != high:
    round_played += 1
    guess = low + (high - low) // 2
    high_low = input("{}. My guess is {}. Should I guess higher or lower?"
                     " Enter h or l, or c if my guess was correct: ".format(round_played, guess)).casefold()
                     # Az bakhshe Code -> Reformat Code : Codemon ro moratab mikone
    if high_low == "h":
        low = guess + 1
    elif high_low == "l":
        high = guess - 1
    elif high_low == "c":
        print("I got it in {}th guesses!".format(round_played))
        break
    else:
        print("please enter h, l or c")
        round_played -= 1
else:
    print("Your number is: {}".format(low))