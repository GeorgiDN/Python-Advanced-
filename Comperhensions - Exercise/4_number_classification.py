def read_input():
    return list(map(int, input().split(", ")))


def find_positive(numbers):
    result = [x for x in numbers if x >= 0]
    return result


def find_negative(numbers):
    result = [x for x in numbers if x < 0]
    return result


def find_even(numbers):
    result = [x for x in numbers if x % 2 == 0]
    return result


def find_odd(numbers):
    result = [x for x in numbers if x % 2 != 0]
    return result


def print_results(numbers):
    print(f"Positive: {', '.join(str(x) for x in find_positive(numbers))}")
    print(f"Negative: {', '.join(str(x) for x in find_negative(numbers))}")
    print(f"Even: {', '.join(str(x) for x in find_even(numbers))}")
    print(f"Odd: {', '.join(str(x) for x in find_odd(numbers))}")


print_results(read_input())
