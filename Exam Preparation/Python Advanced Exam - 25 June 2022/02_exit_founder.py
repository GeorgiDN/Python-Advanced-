import re
from collections import deque

ROWS = 6
players = deque(input().split(', '))
matrix = [input().split() for _ in range(ROWS)]
_exit, trap, wall, empty, winner = 'E', 'T', 'W', '.', False
player_in_trap = []
players_in_rest = deque()

while True:

    curr_player = players.popleft()
    direction = input().strip()
    moves = list(map(int, re.findall(r'\d+', direction)))
    row, col = moves[0], moves[1]

    if curr_player in players_in_rest:
        players_in_rest.popleft()
        players.append(curr_player)
        continue

    if matrix[row][col] == trap:
        winner = players.popleft()
        print(f'{curr_player} is out of the game! The winner is {winner}.')
        break

    elif matrix[row][col] == _exit:
        winner = curr_player
        print(f'{curr_player} found the Exit and wins the game!')
        break

    elif matrix[row][col] == wall:
        players_in_rest.append(curr_player)
        print(f'{curr_player} hits a wall and needs to rest.')

    players.append(curr_player)
