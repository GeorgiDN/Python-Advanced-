numbers = list(map(float, input().split(" ")))
numbers_counter = {}

for num in numbers:
    if num not in numbers_counter:
        numbers_counter[num] = 1
    else:
        numbers_counter[num] += 1

for key, value in numbers_counter.items():
    print(f"{key} - {value} times")
  
