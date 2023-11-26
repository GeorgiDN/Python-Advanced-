numbers = list(map(int, input().split()))
target = int(input())

for i in range(len(numbers)):
    if numbers[i] == '':
        continue
    for j in range(len(numbers)):
        if numbers[j] == '':
            continue
        if numbers[i] + numbers[j] == target:
            print(f'{numbers[i]} + {numbers[j]} = {target}')
            numbers[i] = ''
            numbers[j] = ''
            break
          
