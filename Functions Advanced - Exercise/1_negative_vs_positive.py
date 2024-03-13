def sum_positive_numbers(nums):
    return sum([n for n in nums if n > 0])


def sum_negative_numbers(nums):
    return sum([n for n in nums if n < 0])


def main():
    list_with_numbers = [int(x) for x in input().split()]
    result = ''
    positive_sum = sum_positive_numbers(list_with_numbers)
    negative_sum = sum_negative_numbers(list_with_numbers)

    result += f"{negative_sum}\n"
    result += f"{positive_sum}\n"

    if abs(positive_sum) < abs(negative_sum):
        result += "The negatives are stronger than the positives"
    else:
        result += "The positives are stronger than the negatives"

    return print(result)


if __name__ == '__main__':
    main()



# def sort_numbers():
#     [negatives.append(x) for x in numbers if x < 0]
#     [positives.append(x) for x in numbers if x >= 0]


# numbers = [int(x) for x in input().split()]
# negatives, positives = [], []

# sort_numbers()

# print(sum(negatives))
# print(sum(positives))

# if abs(sum(negatives)) > sum(positives):
#     print("The negatives are stronger than the positives")
# else:
#     print("The positives are stronger than the negatives")




# def negative_vs_positive(nums):
#     negative_sum = []
#     positive_sum = []
#     for num in nums:
#         if num < 0:
#             negative_sum.append(num)
#         elif num > 0:
#             positive_sum.append(num)

#     total_negative = (sum(negative_sum))
#     total_positive = (sum(positive_sum))

#     print(total_negative)
#     print(total_positive)

#     if abs(total_negative) > total_positive:
#         print("The negatives are stronger than the positives")
#     elif abs(total_negative) < total_positive:
#         print("The positives are stronger than the negatives")


# numbers = negative_vs_positive(list(map(int, input().split(" "))))



