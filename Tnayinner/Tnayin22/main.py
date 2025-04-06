number = int(input("Մուտքագրեք թիվը: "))
new_list = [2, 7, 11, 15, 13, 3, 10, 0]
result = []

def find_subsets(lst):
    subsets = [[]]
    for num in lst:
        new_subsets = []
        for subset in subsets:
            new_subsets.append(subset + [num])
        subsets.extend(new_subsets)
    return subsets

for subset in find_subsets(new_list):
    if subset and sum(subset) == number:
        result.append(subset)

print(result)