new_list = [1, 3, 2, 20, 33, 4, 6]
for i in range(len(new_list)):
    max = i
    for j in range(i + 1, len(new_list)):
        if new_list[j] > new_list[max]:
            max = j
        new_list[i], new_list[max] = new_list[max], new_list[i]
print(new_list)