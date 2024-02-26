from collections import deque

players = input().split()
step = int(input())
players = deque(players)

counter = 0

while len(players) > 1:
    counter += 1
    current_player = players.popleft()
    if counter == step:
        print(f"Removed {current_player}")
        counter = 0
    else:
        players.append(current_player)

print(f"Last is {players.popleft()}")




# from collections import deque

# players = input().split()
# step = int(input())
# players = deque(players)


# while len(players) > 1:
#     for _ in range(step - 1):
#         players.append(players.popleft())
#     print(f"Removed {players.popleft()}")

# print(f"Last is {players.popleft()}")




# from _collections import deque

# name_of_players = input().split(' ')
# step_of_hot_potato = int(input())
# players_deque = deque(name_of_players)
# counter = 0

# while len(players_deque) > 1:
#     counter += 1
#     current_name_of_player = players_deque.popleft()

#     if counter == step_of_hot_potato:
#         print(f'Removed {current_name_of_player}')
#         counter = 0
#     else:
#         players_deque.append(current_name_of_player)

# print(f'Last is {players_deque[0]}')
