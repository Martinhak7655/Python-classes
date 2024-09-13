x = 10

fib_list = [1, 2]

for i in range(2, x):
    hajordox_tiv = 0
    for j in range(-2, 0):
        hajordox_tiv += fib_list[i + j]
    fib_list.append(hajordox_tiv)
print(fib_list)