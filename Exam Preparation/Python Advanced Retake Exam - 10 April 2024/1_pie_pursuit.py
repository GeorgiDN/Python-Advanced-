# https://judge.softuni.org/Contests/Practice/Index/4528#0

from collections import deque

contestants_values = deque(map(int, input().split()))
pies = list(map(int, input().split()))

while contestants_values and pies:
    contestant = contestants_values.popleft()
    pie_piece = pies.pop()

    if contestant > pie_piece:
        contestant -= pie_piece
        contestants_values.append(contestant)

    elif contestant < pie_piece:
        pie_piece -= contestant
        pies.append(pie_piece)

        if pie_piece == 1:
            if len(pies) >= 2:
                pies.pop()
                pies[-1] += 1

if not pies and not contestants_values:
    print("We have a champion!")
elif contestants_values:
    print("We will have to wait for more pies to be baked!")
    print(f"Contestants left: {', '.join(map(str, contestants_values))}")
elif pies:
    print("Our contestants need to rest!")
    print(f"Pies left: {', '.join(map(str, pies))}")




# from collections import deque
#
# contestants_values = deque(map(int, input().split()))
# pie = list(map(int, input().split()))
#
# while contestants_values and pie:
#     contestant = contestants_values.popleft()
#     pie_piece = pie.pop()
#
#     if contestant > pie_piece:
#         contestant -= pie_piece
#         contestants_values.append(contestant)
#
#     elif contestant < pie_piece:
#         pie_piece -= contestant
#         pie.append(pie_piece)
#
#         if pie_piece == 1:
#             if len(pie) >= 2:
#                 pie.pop()
#                 pie[-1] += 1
#
# if not pie and len(contestants_values) > 0:
#     print("We will have to wait for more pies to be baked!")
#     print(f"Contestants left: {', '.join(map(str, contestants_values))}")
# elif len(pie) > 0 and not contestants_values:
#     print("Our contestants need to rest!")
#     print(f"Pies left: {', '.join(map(str, pie))}")
# else:
#     print("We have a champion!")


