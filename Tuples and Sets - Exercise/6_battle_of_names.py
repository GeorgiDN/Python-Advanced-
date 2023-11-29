def calculate_ascii_sum(name, row):
    ascii_sum = sum(ord(ch) for ch in name)
    return ascii_sum // row


n = int(input())
odd_numbers = set()
even_numbers = set()

for row in range(1, n + 1):
    name = input()
    ascii_sum = calculate_ascii_sum(name, row)

    if ascii_sum % 2 == 0:
        even_numbers.add(ascii_sum)
    else:
        odd_numbers.add(ascii_sum)

total_even_sum = sum(even_numbers)
total_odd_sum = sum(odd_numbers)

if total_even_sum == total_odd_sum:
    result = even_numbers.union(odd_numbers)
elif total_even_sum > total_odd_sum:
    result = even_numbers.symmetric_difference(odd_numbers)
else:
    result = sorted(odd_numbers, reverse=True)

print(', '.join(map(str, result)))
