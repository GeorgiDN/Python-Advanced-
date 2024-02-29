list_numbers = [int(x) for x in input().split()]
target = int(input())
matches = []
used_numbers = []

idx = 0
while True:
    if idx + 1 > len(list_numbers):
        break

    num1 = list_numbers[idx]

    for num2 in list_numbers:
        if num2 != num1:
            if num2 not in used_numbers and num1 not in used_numbers:
                if num1 + num2 == target:
                    matches.append([num1, num2])
                    used_numbers.append(num2)
    idx += 1

for data in matches:
    n1, n2 = data[0], data[1]
    print(f"{n1} + {n2} = {target}")




# numbers = list(map(int, input().split()))
# target = int(input())

# for i in range(len(numbers)):
#     if numbers[i] == '':
#         continue
#     for j in range(len(numbers)):
#         if numbers[j] == '':
#             continue
#         if numbers[i] + numbers[j] == target:
#             print(f'{numbers[i]} + {numbers[j]} = {target}')
#             numbers[i] = ''
#             numbers[j] = ''
#             break
          
