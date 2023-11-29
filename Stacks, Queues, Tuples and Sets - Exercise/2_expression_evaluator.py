
# 100/100
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
            result = int(result / numbers[i])
    numbers.clear()
    numbers.append(result)


expression = input().split()
current_numbers = []
operators = ("*", "+", "-", "/")
for item in expression:
    if item not in operators:
        current_numbers.append(int(item))
    else:
        evaluate_numbers(item, current_numbers)

print(*current_numbers)
