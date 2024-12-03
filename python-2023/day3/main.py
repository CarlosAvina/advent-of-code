directions = [[0, -1], [1, 0], [0, 1], [-1, 0]]


def isSymbol(char):
    if char is not None and char != "." and not char.isnumeric():
        return True
    return False


def walk(grid, current, nums):
    item = None
    try:
        item = grid[current.y][current.x]
    except:
        item = None

    print(item)

    if item is not None and item.isnumeric():
        nums.append(item)
        return
    if item is None:
        return
    if item == ".":
        return

    grid[current.y][current.x] = "."

    for _, dir in enumerate(directions):
        newCurrent = {"x": current.x + dir[0], "y": current.y + dir[1]}
        walk(grid, newCurrent, nums)


with open("input.txt", "r") as file:
    contents = file.read()

rows = contents.split("\n")
nums = []

for i, row in enumerate(rows):
    for j, char in enumerate(row):
        if isSymbol(char):
            walk(rows, {"x": j, "y": i}, nums)
