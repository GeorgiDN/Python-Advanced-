number_names = int(input())
print('\n'.join(set([name for _ in range(number_names) for name in input().split()])))


# number = int(input())
# unique_names = [input() for _ in range(number)]
# set_unique_names = set(unique_names)

# for name in set_unique_names:
#     print(name)



# def input_lines(num):
#     users = set()
#     for _ in range(num):
#         users.add(input())
#     return users
#
#
# def print_result(users):
#     for user in users:
#         print(user)
#
#
# print_result(input_lines(int(input())))

  
