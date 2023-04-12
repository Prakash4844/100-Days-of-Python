import Art

print(Art.logo)


def add(n1, n2):
    """returns Sum of Integer or Float values"""
    return n1 + n2


def sub(n1, n2):
    """returns Difference of Integer or Float values"""
    return n1 - n2


def mul(n1, n2):
    """returns multiplication Integer or Float values"""
    return n1 * n2


def div(n1, n2):
    """returns Division of Integer or Float values as Float"""
    return n1 / n2


def floor_div(n1, n2):
    """returns Division of Integer or Float values as Integer"""
    return n1 // n2


operations = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div,
    "//": floor_div,
}


def calc():
    should_continue = True
    answer = 0

    while should_continue:

        if not answer:
            num1 = float(input("Enter a no: "))
        else:
            num1 = answer

        for symbol in operations:
            print(symbol)

        opr = input("Choose the symbol you want to perform from above: ")

        num2 = float(input("Enter another no: "))

        if opr == "+" or opr == "-" or opr == "*" or opr == "/" or opr == "//":
            answer = operations[opr](num1, num2)
        else:
            answer = "Invalid Operation."

        print(f"{num1} {opr} {num2} = {answer}")

        if answer == "Invalid Operation.":
            exit()

        rerun = input("Should we continue? Press y|Y to for YES and press n to exit OR to Restart the calc "
                      "press r|R: "
                      "").lower()
        if rerun == 'y':
            num1 = answer
        elif rerun == 'r':
            calc()
        elif rerun == 'n':
            should_continue = False


calc()
print("Have A Good Day...")
