#1 GREL FUNCTION VORPES ARGUMENT STANUMA ZANGVACY, U VERADARCNUMA TVERI GUMARY
#2 GREL FUNCTION VORY KVERADARCNI AMENAMEC TIVY U POQR
#3 GREL FUNCTION VORY VERADARZNUMA ZANGVAC VORI MEJ KLINEN ZUYG TVER
#4 GREL FUNCTION EV HERTAKANUTYUNY POXEL
#5 GREL FUNCTION BAYC STANAL MECUTYAMB ERKORD TIVY
#6 GREL FUNCTION VORY VERADARZNUMA TRVAC ARGUMENTI HAVASARUMY ZANGVACOV
#7 GREL FUNCTION VORI MEJ TVERY DASAVORVAC KLINEN AJMAN KARGOV
#8 GREL FUNCTION VORY ZANGVACY KVERADARCNI XARY TESQOV

import random


new_list = [7, 5, 4, 9, 1, 4, 3]

#1

# def f(list):
#     gumar = 0
#     for i in list:
#         gumar += i
#     return gumar

# print(f(new_list))

#2

# def max_min(list):
#     max = list[0]
#     min = list[0]

#     for i in range(1, len(list)):
#         if list[i] >= max:
#             max = list[i]
#         elif list[i] <= min:
#             min = list[i]
#     return max, min

# max, min = max_min(new_list)
# print(max)
# print(min)

#3 

# def get_couple_numbers(list):
#     num_list = []
#     for i in list:
#         if i % 2 == 0 and i not in num_list:
#             num_list.append(i)
#     return num_list

# patasxan = get_couple_numbers(new_list)
# print(patasxan)

#4

# def reverse_list(list):
#     for i in range(int(len(new_list) // 2)):
#         element1 = list[i]
#         element2 = list[len(list)-1-i]

#         list[i] = element2
#         list[len(list)-1-i] = element1
#     return list

# patasxan = reverse_list(new_list)
# print(patasxan)

#5

# def f(list):
#     arajin = list[0]
#     erkrord = list[0]

#     for i in list:
#         if i > arajin:
#             erkrord = arajin
#             arajin = i
#         elif i > erkrord and i != arajin:
#             erkrord = i

#     return erkrord

# print(f(new_list))

#6 

# def f(list, target):
#     list2 = []
#     for i in range(len(list)):
#         for j in range(i + 1, len(list)):
#             if list[i] + list[j] == target:
#                 list2.append([list[i], list[j]])
#     return list2
# print(f(new_list, 10))

#7

# def f(list):
#     x = len(list)
#     for i in range(x):
#         for j in range(0, x - i - 1):
#             if list[j] > list[j+1]:
#                 list[j], list[j+1] = list[j+1], list[j]
#     return list

# print(f(new_list))

#8

def f(list):
    x = len(list)

    for i in range(x):
        j = random.randint(i, x - 1)
        list[i], list[j] = list[j], list[i]
    return list

print(f(new_list))