points_number = int(input())
longest_intersection = []

for _ in range(points_number):
    intersection_points_data = input().split("-")
    first_point, second_point = intersection_points_data[0].split(",")
    first_point, second_point = int(first_point), int(second_point)

    third_point, fourth_point = intersection_points_data[1].split(",")
    third_point, fourth_point = int(third_point), int(fourth_point)

    current_intersection = []
    for num in range(first_point, second_point + 1):
        if num in range(third_point, fourth_point+1):
            current_intersection.append(num)

    if sum(current_intersection) > sum(longest_intersection):
        longest_intersection = current_intersection

print(f"Longest intersection is {longest_intersection} with length {len(longest_intersection)}")



# n = int(input())

# first_check = []
# second_check = []

# final_list = []

# for _ in range(n):
#     info = input()
#     separated_ranges = info.replace('-', ',')
#     ranges = [int(x) for x in separated_ranges.split(',')]

#     for num1 in range(ranges[0], (ranges[1]+1)):
#         first_check.append(num1)

#     for num2 in range(ranges[2], (ranges[3]+1)):
#         if num2 in first_check:
#             second_check.append(num2)

#     if len(final_list) < len(second_check):
#         final_list = second_check

#     first_check = []
#     second_check = []


# print(f"Longest intersection is {final_list} with length {len(final_list)}")
