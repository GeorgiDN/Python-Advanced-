from collections import deque

bees = deque(map(int, input().split()))
eaters = list(map(int, input().split()))


while bees and eaters:
    bee = bees.popleft()
    attacker = eaters.pop()

    possible_kills = attacker * 7

    if possible_kills > bee:
        attacker -= bee // 7
        eaters.append(attacker)

    elif possible_kills < bee:
        bee -= attacker * 7
        bees.append(bee)

print("The final battle is over!")

if not bees and not eaters:
    print("But no one made it out alive!")
if bees:
    print(f"Bee groups left: {', '.join(map(str, bees))}")
if eaters:
    print(f"Bee-eater groups left: {', '.join(map(str, eaters))}")




########################################################################
# from collections import deque
# 
# 
# bee_groups = deque(map(int, input().split()))
# eaters = list(map(int, input().split()))
# 
# while bee_groups and eaters:
#     bee = bee_groups.popleft()
#     attacker = eaters.pop()  # eater
# 
#     attackers_needed = bee // 7
# 
#     if bee < attacker * 7:
#         attacker -= attackers_needed
#         eaters.append(attacker)
# 
#     elif attacker * 7 < bee:
#         bee -= attacker * 7
#         bee_groups.append(bee)
# 
#     elif bee == attacker * 7:
#         continue
# 
# print('The final battle is over!')
# if not eaters and not bee_groups:
#     print('But no one made it out alive!')
# else:
#     if bee_groups:
#         print(f'Bee groups left: {", ".join(map(str, bee_groups))}')
#     if eaters:
#         print(f'Bee-eater groups left: {", ".join(map(str, eaters))}')


####################################################################################
# from collections import deque
#
# bee_groups = deque(map(int, input().split()))
# bee_eaters = list(map(int, input().split()))
#
# while bee_eaters and bee_groups:
#     bees = bee_groups.popleft()
#     eater = bee_eaters.pop()
#
#     if eater * 7 > bees:
#         left_eaters = eater - (bees // 7)
#         bee_eaters.append(left_eaters)
#     elif eater * 7 < bees:
#         left_bees = bees - (eater * 7)
#         bee_groups.append(left_bees)
#     else:
#         continue
#
# print("The final battle is over!")
# if not bee_groups and not bee_eaters:
#     print("But no one made it out alive!")
#
# if bee_groups:
#     str_bees = ", ".join(map(str, bee_groups))
#     print(f"Bee groups left: {str_bees}")
#
# if bee_eaters:
#     str_eaters = ", ".join(map(str, bee_eaters))
#     print(f"Bee-eater groups left: {str_eaters}")




# from collections import deque
#
#
# def battle():
#
#     bees = deque(map(int, input().split()))
#     bee_eaters = list(map(int, input().split()))
#
#     while bees and bee_eaters:
#         current_bees = bees[0]
#         current_bee_eaters = bee_eaters[-1]
#
#         if current_bee_eaters * 7 > current_bees:
#             bee_eaters_left = current_bee_eaters - (current_bees // 7)
#             bees.popleft()
#             bee_eaters[-1] = bee_eaters_left
#
#         elif current_bee_eaters * 7 < current_bees:
#             remaining_bees = current_bees - (current_bee_eaters * 7)
#             bee_eaters.pop()
#             bees.popleft()
#             bees.append(remaining_bees)
#
#         else:
#             bees.popleft()
#             bee_eaters.pop()
#
#     print("The final battle is over!")
#     if not bees and not bee_eaters:
#         print("But no one made it out alive!")
#     elif bees:
#         print("Bee groups left:", ", ".join(map(str, bees)))
#     elif bee_eaters:
#         print("Bee-eater groups left:", ", ".join(map(str, bee_eaters)))
#
#
# battle()
