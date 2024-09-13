user = input("Enter Your Text")
i = 0
qanak1 = 0
qanak2 = 0
while i < len(user):
    if user[i] == "a":
        qanak1 += 1
    elif user[i] == "A":
        qanak2 += 1
    i += 1
print(qanak1)
print(qanak2)