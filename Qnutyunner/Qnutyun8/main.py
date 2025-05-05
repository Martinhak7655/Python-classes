import random

board = []
for i in range(10):
    row = []
    for j in range(10):
        row.append("")
    board.append(row)

while True:
    enter_min = int(input("Նշեք ականների քանակը 1 ից մինչև 99։ "))
    if enter_min < 1 or enter_min > 99:
        print("խնդրում եմ ընտրեք ականների քանակը 1 ից մինչև 99")
    else:
        break

mines = []

while len(mines) < enter_min:
    x = random.randint(0, 9)
    y = random.randint(0, 9)
    if [x, y] not in mines:
        mines.append([x, y])

miavor = 0

while True:
    for row in board:
        print(row)
    
    answer = input("Մուտք արեք տող և սյուն՝ օրինակ՝ 2 4, կամ վերջ։  ")
    if answer == "վերջ":
        print(f"Խաղը ավարտվեց քո միավորներն են {miavor}")
        break

    row, col = map(int, answer.split())

    if row < 0 or row > 9 or col < 0 or col > 9:
        print("Տաղտակից դուրս")
        continue

    if [row, col] in mines:
        board[row][col] = "*"
        print("Դուք պարտվեցիք, քանի որ կայնեցիք ականի վրա")
        break
    elif board[row][col] == "O":
        print("Դուք արդեն ընտրելեք այս դաշտը")
    else:
        board[row][col] = "O"
        miavor += 1

