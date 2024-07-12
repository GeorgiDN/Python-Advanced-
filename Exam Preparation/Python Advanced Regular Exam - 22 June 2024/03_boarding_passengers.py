def boarding_passengers(*args):

    capacity_of_ship = int(args[0])
    rest = args[1:]
    passengers_left = len(rest)
    passengers_on_board = {}
    all_on_the_board = True

    for number_of_passengers, benefit_name in rest:
        if capacity_of_ship == 0:
            break

        if capacity_of_ship >= number_of_passengers:
            if benefit_name not in passengers_on_board:
                passengers_on_board[benefit_name] = 0
            passengers_on_board[benefit_name] += number_of_passengers
            passengers_left -= 1
            capacity_of_ship -= number_of_passengers
        else:
            all_on_the_board = False

    sorted_data = sorted(passengers_on_board.items(), key=lambda x: (-x[1], (x[0])))

    result = ''
    result += 'Boarding details by benefit plan:\n'

    for plan, count in sorted_data:
        result += f'## {plan}: {count} guests\n'

    if passengers_left == 0 and all_on_the_board:
        result += "All passengers are successfully boarded!"

    elif capacity_of_ship == 0 and passengers_left > 0:
        result += "Boarding unsuccessful. Cruise ship at full capacity."

    elif capacity_of_ship > 0 and not all_on_the_board:
        result += f"Partial boarding completed. Available capacity: {capacity_of_ship}."

    return result


# print(boarding_passengers(150, (35, 'Diamond'), (55, 'Platinum'), (35, 'Gold'), (25, 'First Cruiser')))
#print(boarding_passengers(100, (20, 'Diamond'), (15, 'Platinum'), (25, 'Gold'), (25, 'First Cruiser'), (15, 'Diamond'), (10, 'Gold')))
#print(boarding_passengers(120, (30, 'Gold'), (20, 'Platinum'), (30, 'Diamond'), (10, 'First Cruiser'), (31, 'Platinum'), (20, 'Diamond')))
