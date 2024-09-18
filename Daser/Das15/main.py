# new_list = [1, 2, 3, 4, 5]
# user = int(input("Enter Your Number >>> "))

    
# if new_list.count(user) == 0:
#     new_list.append(user)
# else:
#     new_list.remove(user)
# print(new_list)

new_list = [1, 2, 3, 4, 5]

max = max(new_list)
min = min(new_list)

min, max = max, min
new_list.clear()
new_list.append(min)
new_list.append(max)
print(new_list)