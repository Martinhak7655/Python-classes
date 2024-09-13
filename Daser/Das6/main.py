# new_list = [1, 3, 2, 20, 33, 4, 6]

# gumar = 0

# for i in range(0, len(new_list)):
#     gumar += new_list[i]
# print(gumar)

# new_list = [1, 3, 2, 20, 33, 4, 6]
# gumar = 0

# for i in new_list:
#     gumar+=i
# print(gumar)

# new_list = [1, 3, 2, 20, 33, 4, 6]
# gumar = 0
# for i in range(0, len(new_list)):
#     if not(new_list[i] % 2 == 0):
#         gumar+=new_list[i]
# print(gumar)

# new_list = [1, 3, 2, 20, 33, 4, 6]
# gumar = 0

# for i in new_list:
#     if not(i % 2 == 0):
#         gumar+=i
# print(gumar)

# new_list = [1, 3, 2, 20, 33, 4, 6]

# for i in range(len(new_list)-1, 0, -1):
#     print(new_list[i])

# new_list = [1, 3, 2, 20, 33, 4, 6]
# max = new_list[0]
# min = new_list[0]

# for i in range(1, len(new_list)):
#     if new_list[i] >= max:
#         max = new_list[i]
#     elif new_list[i] <= min:
#         min = new_list[i]


# x = min
# min = max
# max = x

# print(max)
# print(min)

new_list = [1, 3, 2, 20, 33, 4, 6]
x = len(new_list)
for i in range(x):
    for j in range(0, x - i - 1 ):
        if new_list[j] > new_list[j+1]:
            new_list[j], new_list[j+1] = new_list[j+1], new_list[j]
print(new_list)