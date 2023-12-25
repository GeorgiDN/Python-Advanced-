start_num = int(input())
end_num = int(input())

divisible_numbers = [num for num in range(start_num, end_num + 1) if any(num % div == 0 for div in range(2, 10 + 1))]

print(divisible_numbers)
