def sort_numbers():
    [negatives.append(x) for x in numbers if x < 0]
    [positives.append(x) for x in numbers if x >= 0]


numbers = [int(x) for x in input().split()]
negatives, positives = [], []

sort_numbers()

print(sum(negatives))
print(sum(positives))

if abs(sum(negatives)) > sum(positives):
    print("The negatives are stronger than the positives")
else:
    print("The positives are stronger than the negatives")




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



