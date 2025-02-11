from collections import deque

seats = input().split(', ')
rotations, taken_seats = 0, []
first_sequence = deque(map(int, input().split(', ')))
second_sequence = deque(map(int, input().split(', ')))

while True:
    if rotations == 10 or len(taken_seats) == 3:
        break

    first = first_sequence.popleft()
    second = second_sequence.pop()

    char = chr(first + second)

    seat_place_1 = f'{first}{char}'
    seat_place_2 = f'{second}{char}'

    if seat_place_1 in seats and seat_place_1 not in taken_seats:
        taken_seats.append(seat_place_1)
    elif seat_place_2 in seats and seat_place_2 not in taken_seats:
        taken_seats.append(seat_place_2)
    else:
        first_sequence.append(first)
        second_sequence.appendleft(second)

    rotations += 1

print(f'Seat matches: {", ".join(taken_seats)}')
print(f'Rotations count: {rotations}')
