from basic_calculations import calculations

data = input().split()
number1, current_operator, number2 = float(data[0]), data[1], int(data[2])

print(calculations.calculate_numbers(number1, current_operator, number2))
