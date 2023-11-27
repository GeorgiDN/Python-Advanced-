length_of_two = input().split(' ')
number_1 = int(length_of_two[0])
number_2 = int(length_of_two[1])

list_1 = []
list_2 = []
repeat = []

for i in range(number_1):
    number = int(input())
    if number not in list_1:
        list_1.append(number)

for j in range(number_2):
    number2 = int(input())
    if number2 not in list_2:
        list_2.append(number2)

for num in list_1:
    if num in list_2:
        repeat.append(num)

for curr_num in repeat:
    print(''.join(str(curr_num)))
  



# def input_lines(num):
#     lines = set()
#     for _ in range(num):
#         lines.add(input())
#     return lines
#
#
# def intersection(a, b):
#     return a.intersection(b)
#
#
# def print_result(res):
#     for r in res:
#         print(r)
#
#
# len1, len2 = input().split(" ")
#
# line1 = input_lines(int(len1))
# line2 = input_lines(int(len2))
#
# print_result(intersection(line1, line2))
