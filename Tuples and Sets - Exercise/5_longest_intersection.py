n = int(input())

first_check = []
second_check = []

final_list = []

for _ in range(n):
    info = input()
    separated_ranges = info.replace('-', ',')
    ranges = [int(x) for x in separated_ranges.split(',')]

    for num1 in range(ranges[0], (ranges[1]+1)):
        first_check.append(num1)

    for num2 in range(ranges[2], (ranges[3]+1)):
        if num2 in first_check:
            second_check.append(num2)

    if len(final_list) < len(second_check):
        final_list = second_check

    first_check = []
    second_check = []


print(f"Longest intersection is {final_list} with length {len(final_list)}")
