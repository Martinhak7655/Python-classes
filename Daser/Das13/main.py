number = input("Enter Your Number >>>  ")

def f(n):
    for i in range(2, int(n)):
        if (int(n) % i) == 0:
            return f"{n} Sa baxadryal  Tive"
    return f"{n} Sa parz  Tive"

for z in number:
    print(f(z))