input_string=input("Enter a string:")
mySet = set(input_string) # To create a set of all the characters present in the input string by
for element in mySet:
    countOfChar = 0
    for character in input_string:
        if character == element:
            countOfChar += 1
    print("Count of",element,"is",countOfChar)
