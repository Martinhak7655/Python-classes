new_list = [4, 2, 5, 7]
new_list2 = []

for i in new_list:
    factorial = 1
    for j in range(1, i + 1):
        factorial *= j
    new_list2.append(factorial)
print(new_list2)   