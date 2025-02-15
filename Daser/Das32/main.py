from ask import ask_number1, ask_number2, ask_char
from middleware import midd

def run_app():
    num1 = ask_number1()
    num2 = ask_number2()
    charachter = ask_char()
    return print(midd(charachter, num1, num2 ))

if __name__ == "__main__":
    run_app()
