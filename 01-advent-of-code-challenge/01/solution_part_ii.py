def find_calories(filename):

    with open(filename, "r") as list:
        input = list.read()

    elf_list = input.split("\n")
    calories = []
    current_calories = 0

    for elf in elf_list:
        if elf == '':
            calories.append(current_calories)
            current_calories = 0
        else:
            current_calories += int(elf)

    calories.append(current_calories)
    calories = sorted(calories, reverse=True)

    top_three = calories[:3]
    return sum(top_three)

filename = "01-advent-of-code-challenge/01/sample.in"
print(find_calories(filename))