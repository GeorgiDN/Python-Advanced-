def print_result(result_):
    print(', '.join(map(str, result_)))


def fill_the_sets_with_sum(evens_, odds_, ascii_sum_):
    if ascii_sum_ % 2 == 0:
        evens_.add(ascii_sum_)
    else:
        odds_.add(ascii_sum_)

    return evens_, odds_


def fill_the_result(result_, evens_, odds_):
    for num in evens_:
        result_.add(num)

    for num in odds_:
        result_.add(num)

    return result_


def main():
    names_number = int(input())

    evens = set()
    odds = set()

    for row in range(1, names_number + 1):
        name = input()
        ascii_sum = 0

        for char in name:
            ascii_sum += ord(char)

        ascii_sum //= row

        evens, odds = fill_the_sets_with_sum(evens, odds, ascii_sum)

    result = set()
    if sum(evens) >= sum(odds):
        result = fill_the_result(result, evens, odds)

    elif sum(evens) < sum(odds):
        result = odds

    print_result(result)


if __name__ == "__main__":
    main()




# def calculate_ascii_sum(name, row):
#     ascii_sum = sum(ord(ch) for ch in name)
#     return ascii_sum // row


# n = int(input())
# odd_numbers = set()
# even_numbers = set()

# for row in range(1, n + 1):
#     name = input()
#     ascii_sum = calculate_ascii_sum(name, row)

#     if ascii_sum % 2 == 0:
#         even_numbers.add(ascii_sum)
#     else:
#         odd_numbers.add(ascii_sum)

# total_even_sum = sum(even_numbers)
# total_odd_sum = sum(odd_numbers)

# if total_even_sum == total_odd_sum:
#     result = even_numbers.union(odd_numbers)
# elif total_even_sum > total_odd_sum:
#     result = even_numbers.symmetric_difference(odd_numbers)
# else:
#     result = sorted(odd_numbers, reverse=True)

# print(', '.join(map(str, result)))
