def calculator(num1, sign, num2):
    result = None
    if sign == '/':
        result = num1 / num2
    elif sign == '*':
        result = num1 * num2
    elif sign == '-':
        result = num1 - num2
    elif sign == '+':
        result = num1 + num2
    elif sign == '^':
        result = num1 ** num2

    return f"{result:.2f}"
  
