operations = {
    "+": add,
    "-": subtract,
    "*": multiply, 
    "/": divide,
}

num1=int(input("what is the first number:"))
num2=int(input("What is the second number:"))

for symbol in operations:
    print(symbol)
