def boarding_passengers(capacity, *args):
    boarding = {}
    all_boarded = True

    for num_of_passengers, program in args:
        if capacity >= num_of_passengers:
            if program not in boarding:
                boarding[program] = 0
            boarding[program] += num_of_passengers
            capacity -= num_of_passengers
        else:
            all_boarded = False

    result = ['Boarding details by benefit plan:']
    sorted_boarding = dict(sorted(boarding.items(), key=lambda x: (-x[1], x[0])))

    for plan, total_number_of_passangers in sorted_boarding.items():
        result.append(f'## {plan}: {total_number_of_passangers} guests')

    if all_boarded:
        result.append('All passengers are successfully boarded!')
    elif not all_boarded and capacity == 0:
        result.append('Boarding unsuccessful. Cruise ship at full capacity.')
    elif not all_boarded and capacity > 0:
        result.append(f'Partial boarding completed. Available capacity: {capacity}.')

    return '\n'.join(result)


print(boarding_passengers(150, (35, 'Diamond'), (55, 'Platinum'), (35, 'Gold'), (25, 'First Cruiser')))
print(boarding_passengers(100, (20, 'Diamond'), (15, 'Platinum'), (25, 'Gold'), (25, 'First Cruiser'), (15, 'Diamond'), (10, 'Gold')))
print(boarding_passengers(120, (30, 'Gold'), (20, 'Platinum'), (30, 'Diamond'), (10, 'First Cruiser'), (31, 'Platinum'), (20, 'Diamond')))



#######################################################################################################################
# def boarding_passengers(*args):
#     capacity_of_ship = int(args[0])
#     passenger_groups = args[1:]
#     all_on_the_board = True
#     board = {}

#     for data in passenger_groups:
#         number_passengers, program_name = int(data[0]), data[1]
#         if capacity_of_ship == 0:
#             all_on_the_board = False
#             break
#         if number_passengers <= capacity_of_ship:
#             if program_name not in board:
#                 board[program_name] = 0
#             board[program_name] += number_passengers
#             capacity_of_ship -= number_passengers
#         else:
#             all_on_the_board = False

#     sorted_board = dict(sorted(board.items(), key=lambda x: (-x[1], x[0])))
#     result = "Boarding details by benefit plan:\n"

#     for benefit_plan, total_number_of_passengers in sorted_board.items():
#         result += f"## {benefit_plan}: {total_number_of_passengers} guests\n"

#     if all_on_the_board:
#         result += "All passengers are successfully boarded!\n"
#     elif capacity_of_ship == 0 and not all_on_the_board:
#         result += "Boarding unsuccessful. Cruise ship at full capacity.\n"
#     elif capacity_of_ship > 0 and not all_on_the_board:
#         result += f"Partial boarding completed. Available capacity: {capacity_of_ship}.\n"

#     return result.strip()





#########################################################################################################################################################################
# def boarding_passengers(*args):

#     capacity_of_ship = int(args[0])
#     rest = args[1:]
#     passengers_left = len(rest)
#     passengers_on_board = {}
#     all_on_the_board = True

#     for number_of_passengers, benefit_name in rest:
#         if capacity_of_ship == 0:
#             break

#         if capacity_of_ship >= number_of_passengers:
#             if benefit_name not in passengers_on_board:
#                 passengers_on_board[benefit_name] = 0
#             passengers_on_board[benefit_name] += number_of_passengers
#             passengers_left -= 1
#             capacity_of_ship -= number_of_passengers
#         else:
#             all_on_the_board = False

#     sorted_data = sorted(passengers_on_board.items(), key=lambda x: (-x[1], (x[0])))

#     result = ''
#     result += 'Boarding details by benefit plan:\n'

#     for plan, count in sorted_data:
#         result += f'## {plan}: {count} guests\n'

#     if passengers_left == 0 and all_on_the_board:
#         result += "All passengers are successfully boarded!"

#     elif capacity_of_ship == 0 and passengers_left > 0:
#         result += "Boarding unsuccessful. Cruise ship at full capacity."

#     elif capacity_of_ship > 0 and not all_on_the_board:
#         result += f"Partial boarding completed. Available capacity: {capacity_of_ship}."

#     return result
