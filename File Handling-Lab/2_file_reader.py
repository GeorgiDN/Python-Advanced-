sum_numbers = 0

with open("numbers.txt") as file:
    for line in file:
        sum_numbers += (int(line))

print(sum_numbers)


# numbers_file = open('numbers.txt', 'r')
# numbers_sum = 0
# for number in numbers_file:
#     numbers_sum += int(number)
# print(numbers_sum)
# numbers_file.close()
