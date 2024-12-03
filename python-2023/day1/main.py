with open("input.txt", "r") as file:
    contents = file.read()

rows = contents.split("\n")
numbers = [
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    0,
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
]

nums_dic = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}
sum = 0

for row in rows:
    lowest = -1
    highest = -1
    first_num = 0
    second_num = 0

    if row == "":
        continue

    for _, num in enumerate(numbers):
        index = row.find(str(num))
        reversed_index = (len(row) - 1) - row[::-1].find(str(num)[::-1])

        if index == -1:
            continue

        if lowest == -1 and highest == -1:
            lowest = index
            highest = reversed_index

        lowest = min(index, lowest)
        highest = max(reversed_index, highest)

        if index == lowest:
            first_num = num
        if reversed_index == highest:
            second_num = num

    final_first_digit = (
        nums_dic[str(first_num)] if len(str(first_num)) > 1 else str(first_num)
    )
    final_second_digit = (
        nums_dic[str(second_num)] if len(str(second_num)) > 1 else str(second_num)
    )

    two_digits_num = final_first_digit + final_second_digit
    sum += int(two_digits_num)
    print(row, " - ", two_digits_num, " | sum: ", sum)

print(sum)
