n, m = list(map(int, input().split()))
set1 = {int(input()) for _ in range(n)}
set2 = {int(input()) for _ in range(m)}
print(*set1.intersection(set2), sep='\n')

# n, m = list(map(int, input().split()))
# print(*{int(input()) for _ in range(n)}.intersection({int(input()) for _ in range(m)}), sep='\n')



# first_set_length, second_set_length = input().split()

# first_set = set()
# second_set = set()

# for _ in range(int(first_set_length)):
#     number = int(input())
#     first_set.add(number)
    
# for _ in range(int(second_set_length)):
#     number = int(input())
#     second_set.add(number)
    
# numbers_in_two_sets = second_set.intersection(first_set)
# [print(num) for num in numbers_in_two_sets]




# length_of_two = input().split(' ')
# first_set_length = int(length_of_two[0])
# second_set_length = int(length_of_two[1])

# list_1 = []
# list_2 = []
# repeat = []

# for num1 in range(first_set_length):
#     number = int(input())
#     if number not in list_1:
#         list_1.append(number)

# for num2 in range(second_set_length):
#     number2 = int(input())
#     if number2 not in list_2:
#         list_2.append(number2)

# for num in list_1:
#     if num in list_2:
#         repeat.append(num)


# print('\n'.join(map(str, [curr_num for curr_num in repeat])))
  




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
