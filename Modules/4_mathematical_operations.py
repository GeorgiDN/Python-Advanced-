from python_advanced.modules_lab.basic_calculations import calculator

inp = input().split()
number1 = float(inp[0])
sign = inp[1]
number2 = int(inp[2])

print(calculator(number1, sign, number2))
