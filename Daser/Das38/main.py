#unenq yndhanur mihat zangvac petqa nenc anenq vor dasavarovi achman kargov
#unenq mihat text petqa aranc voreve method ogtagorcelu lcnenq zangvaci mej karevor payman ete ka krknvox tar chenq avelacnum
#patrastel palindrome ev prabelnery antesel
#tverov mihat zangvac amenamec tivy ev amenapoqr tivy u texerov poxel

# 1
# new_list = [2, 20, 3, 44, 9, 55]
# x = len(new_list)
# for i in range(x):
#     for j in range(0, x - i - 1):
#         if new_list[j] < new_list[j+1]:
#             new_list[j], new_list[j+1] = new_list[j+1], new_list[j]
# print(new_list)

# 2
# text = "hello"
# new_list = []

# for i in text:
#     new_list += [i]

# print(new_list)

#3
# text = "hello"
# new_list = []

# for i in range(len(text)):
#     krknvox = False
#     for j in range(len(new_list)):
#         if text[i] == new_list[j]:
#             krknvox = True
#             break
#     if not krknvox:
#         new_list += text[i]

# print(new_list) 

#4
# name = "a n n a"
# i = 0
# l = len(name) - 1
# palindrome = 0

# while l > i:
#     if name[i] != name[l]:
#         palindrome = 1
#         break
#     l-=1
#     i+=1

# if palindrome == 0:
#     print(f"{name}: Sa palindromee")
# else:
#     print(f"{name}: Sa palindrome che")

#5
# number = int(input("Greq tivy: "))
# new_list = [2, 7, 11, 15, 13, 3, 10, 0]
# result = []

# for i in range(len(new_list)):
#     for j in range(i + 1, len(new_list)):
#         if new_list[i] + new_list[j] == number:
#             result += [[new_list[i], new_list[j]]]

# print(result)

#6
# new_list = [2, 7, 11, 15, 13, 3, 10, 0]
# max = new_list[0]
# min = new_list[0]
# max_index = 0
# min_index = 0

# for i in range(1, len(new_list)):
#     if new_list[i] > max:
#         max = new_list[i]
#         max_index = i
#     if new_list[i] < min:
#         min = new_list[i]
#         min_index = i

# new_list[max_index], new_list[min_index] = new_list[min_index], new_list[max_index]
# print(new_list)

#7
# number = int(input("Greq tivy: "))
# new_list = [2, 7, 11, 15, 13, 3, 10, 0]
# result = []

# for i in range(len(new_list)):
#     for j in range(i + 1, len(new_list)):
#         for k in range(j + 1, len(new_list)):
#             if new_list[i] + new_list[j] + new_list[k] == number:
#                 result += [[new_list[i], new_list[j], new_list[k]]]

# print(result)