def evaluate_numbers(operator, numbers):
    if operator == "*":
        result = 1
        for i in range(len(numbers)):
            result *= numbers[i]
    elif operator == "+":
        result = sum(numbers)
    elif operator == "-":
        result = numbers[0]
        for i in range(1, len(numbers)):
            result -= numbers[i]
    else:
        result = numbers[0]
        for i in range(1, len(numbers)):
            result = result // numbers[i]
    numbers.clear()
    numbers.append(result)


def main():
    expression = input().split()
    current_numbers = []
    operators = ["+", "-", "*", "/"]

    for char in expression:
        if char not in operators:
            current_numbers.append(int(char))
        else:
            evaluate_numbers(char, current_numbers)

    print(*current_numbers)


if __name__ == "__main__":
    main()

