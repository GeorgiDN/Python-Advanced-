file_name = "numbers.txt "
sum_numbers = 0

with open(file_name, "r") as file:
    for num in file:
        sum_numbers += int(num)

print(sum_numbers)
file.close()




# sum_numbers = 0
#
# with open("numbers.txt") as file:
#     for line in file:
#         sum_numbers += (int(line))
#
# print(sum_numbers)




# sum_numbers = 0
#
# with open("numbers.txt") as file:
#     for line in file.readlines():
#         sum_numbers += int(line)
#
# print(sum_numbers)

