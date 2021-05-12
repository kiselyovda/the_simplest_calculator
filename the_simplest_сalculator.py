stop_word = "stop"
reset_word = "reset"
main_phrase = f"\nType '{stop_word}' for stopping calculations, {reset_word} for reset calculations or continue operations: "


def calculations(expression):
    def take_args(expression):
        exception = ["*", "/", "+", "-", "^"]
        count = 0
        x, y = "", ""
        for i in range(len(expression)):
            if expression[i] == "-" and i == 0:
                x += expression[0]
                count += 1
                continue
            if expression[i] in exception:
                count += 1
                method = expression[i]
                break
            x += expression[i]
            count += 1
        for i in expression[count:]:
            y += i

        return x, method, y

    x, method, y = take_args(expression)

    def isFloat(arg):
        return float(arg) if "." in arg else int(arg)

    x = isFloat(x)
    y = isFloat(y)

    if method == "+":
        return x + y
    if method == "-":
        return x - y

    if method == "/":
        return round(x / y, 4)
    if method == "*":
        return x * y
    if method == "^":
        return x ** y
    return False


if __name__ == "__main__":
    expression = input("Input expression: ")
    result = calculations(expression)
    print(result)
    condition = input(main_phrase)

    while condition != stop_word:
        if condition == reset_word:
            expression = input("Input new expression: ")
            result = calculations(expression)
        else:
            result = calculations(f"{result}{condition}")
        print(result)
        condition = input(main_phrase)
