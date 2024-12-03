with open("input.txt", "r") as file:
    contents = file.read()
# 12 red cubes, 13 green cubes, and 14 blue cubes
# cubes = {"red": 12, "green": 13, "blue": 14}
# ids = []
powers = []

games = contents.split("\n")

for index, value in enumerate(games):
    if value == "":
        break

    # possible = True
    sets = value.split(":")[1].split(";")
    maximums = {"red": 0, "green": 0, "blue": 0}

    for individual_set in sets:
        colors = individual_set.split(",")

        for color in colors:
            for i, key in enumerate(list(maximums.keys())):
                if color.find(key) != -1:
                    current = int(color.strip().split(" ")[0])
                    if maximums[key] < current:
                        maximums[key] = current

    power = 1
    for max_color in list(maximums.values()):
        power *= max_color

    powers.append(power)


sum = 0
for item in powers:
    sum += item

print(sum)
