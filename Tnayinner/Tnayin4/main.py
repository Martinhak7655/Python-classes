str = "012345"
new_str = ""
count = 1

for i in range(0, len(str)):
    for x in range(i + 1, len(str)):
        if not(str[i] in new_str ) and str[i] == str[x]:
            count += 1
        if not(str[i] in new_str):
           print(f"{str[i]} - {count}")
        new_str += str[i]
        count = 1

