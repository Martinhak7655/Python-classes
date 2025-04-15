#grel function factorial aranc methdoi
#grel fibonachii hajordakanutyun aranc methodi
#unenq zangvac ira mej xary tvera aranc zangvaci method vor katarvi haylay u aranc methodi
#grel mihat function vory tivy grelis gruma parz e te baxadryal

#1+

# fib_list = [1, 2]

# def fibonachi(x):
#     for i in range(2, x):
#         hajordox_tiv = 0
#         for j in range(-2, 0):
#             hajordox_tiv += fib_list[i + j]
#         fib_list.append(hajordox_tiv)
# fibonachi(19)
# print(fib_list)

#2+

# new_list = [8, 3, 4, 5]
# new_list2 = []

# for i in new_list:
#     factorial = 1
#     for j in range(1, i + 1):
#         factorial *= j
#     new_list2.append(factorial)
# print(new_list2)

#3+

# new_list = [8, 5, 9, 10, 20, 22, 62, 1111, 7]

# for i in range(int(len(new_list) / 2)):
#     element1 = new_list[i]
#     element2 = new_list[len(new_list)-1-i]

#     new_list[i] = element2
#     new_list[len(new_list)-1-i] = element1

# print(new_list)

#4+

# def factorial(num):
#     patasxan = 1
#     for i in range(2, num + 1):
#         patasxan *= i
#     return patasxan

# number = int(input("Mutqagreq tivy: "))
# print(f"{number} i factrialy {factorial(number)}")

#5+
# def number(num):
#     for i in range(2, num):
#         if (num % i) == 0:
#             return "Sa baxadryal tive"
#         if (i == num - 1):
#             return "Sa parz tive "
# user = int(input("Mutqagreq tivy"))
# print(number(user))