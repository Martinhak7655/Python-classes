from controller import gumar, hanum, bazmapatkum, bajanum

def midd(char, number1, number2):
    if char == "+":
        return gumar(number1, number2)
    elif char == "-":
        return hanum(number1, number2)
    elif char == "*":
        return bazmapatkum(number1, number2)
    elif bajanum == "/":
        return bajanum(number1, number2)
    else:
        print("Invalid charachter")