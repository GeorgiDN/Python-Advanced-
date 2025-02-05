from collections import deque


bee_groups = deque(map(int, input().split()))
eaters = list(map(int, input().split()))

while bee_groups and eaters:
    bee = bee_groups.popleft()
    attacker = eaters.pop()  # eater

    attackers_needed = bee // 7

    if bee < attacker * 7:
        attacker -= attackers_needed
        eaters.append(attacker)

    elif attacker * 7 < bee:
        bee -= attacker * 7
        bee_groups.append(bee)

    elif bee == attacker * 7:
        continue

print('The final battle is over!')
if not eaters and not bee_groups:
    print('But no one made it out alive!')
else:
    if bee_groups:
        print(f'Bee groups left: {", ".join(map(str, bee_groups))}')
    if eaters:
        print(f'Bee-eater groups left: {", ".join(map(str, eaters))}')



##########################################################################################################
# from collections import deque

# bee_groups = deque(map(int, input().split()))
# bee_eaters = list(map(int, input().split()))

# while bee_eaters and bee_groups:
#     bees = bee_groups.popleft()
#     eater = bee_eaters.pop()

#     if eater * 7 > bees:
#         left_eaters = eater - (bees // 7)
#         bee_eaters.append(left_eaters)
#     elif eater * 7 < bees:
#         left_bees = bees - (eater * 7)
#         bee_groups.append(left_bees)
#     else:
#         continue

# print("The final battle is over!")
# if not bee_groups and not bee_eaters:
#     print("But no one made it out alive!")

# if bee_groups:
#     str_bees = ", ".join(map(str, bee_groups))
#     print(f"Bee groups left: {str_bees}")

# if bee_eaters:
#     str_eaters = ", ".join(map(str, bee_eaters))
#     print(f"Bee-eater groups left: {str_eaters}")
