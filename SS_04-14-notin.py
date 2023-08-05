acctivity = input("What would you like to do today? ")

if "cinema" not in acctivity.casefold(): # casefold() funcation makes the string lowercase
    print("But I want to go to the cinema")
else:
    print("Let's go cinema together")