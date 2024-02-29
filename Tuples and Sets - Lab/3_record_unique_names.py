names_number = int(input())
names_data = {input() for _ in range(names_number)}

for name in names_data:
    print(name)



# names_number = int(input())
# print('\n'.join([name for name in {input() for _ in range(names_number)}]))




# number_names = int(input())
# number_list = []
#
# for name in range(number_names):
#     curr_name = input()
#     number_list.append(curr_name)
#
# not_repeat_names = set(number_list)
# for n in not_repeat_names:
#     print(n)
#
