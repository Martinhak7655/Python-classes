my_list = [3, 5, 1, 7, 8, 6]
new_list = []

for i in my_list:
    for j in range(2, i + 1):
        if (i % j == 0 and j != i):
            break
        if (i == j):
            new_list.append(i)
print(new_list)

# num = "9867"
# new_number = 0

# for i in range(0, len(num)):
#     new_number += int(num[i])
# print(new_number)

# string = "anna"
# i = 0
# l = len(string) -1 
# palindrome = 0

# while l > i:
#     if string[i] != string[l]:
#         palindrome = 1
#         break
#     l-=1
#     i+=1
# if palindrome == 0:
#     print(f"{string}: Sa palindromee")
# else:
#     print(f"{string}: Sa palindrome che")