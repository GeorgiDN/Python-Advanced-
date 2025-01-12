from collections import deque

price_per_bullet = int(input())
barrel_size = int(input())
bullets = list(map(int, input().split()))
locks = deque(map(int, input().split()))
value_of_intelligence = int(input())
shoot_count = barrel_size
total_bullets = len(bullets)

while bullets and locks:
    shoots = bullets.pop()
    lock = locks.popleft()

    if shoot_count == 0:
        print('Reloading!')
        shoot_count = barrel_size
    shoot_count -= 1

    if lock < shoots:
        print('Ping!')
        locks.appendleft(lock)
    else:
        print('Bang!')

if shoot_count == 0 and bullets:
    print('Reloading!')

if not locks:
    earned = value_of_intelligence - ((total_bullets - len(bullets)) * price_per_bullet)
    print(f'{len(bullets)} bullets left. Earned ${earned}')
elif locks:
    print(f"Couldn't get through. Locks left: {len(locks)}")


# from collections import deque

# bullet_price = int(input())
# gun_barrel_size = int(input())
# bullets = list(map(int, input().split()))       
# locks = deque(list(map(int, input().split()))) 
# prize_of_the_value = int(input())
# number_of_shots = 0

# while bullets:
#     if not locks:
#         break
#     number_of_shots += 1
#     bullet = bullets.pop()
#     prize_of_the_value -= bullet_price
#     if bullet <= locks[0]:
#         print("Bang!")
#         locks.popleft()
#     else:
#         print("Ping!")
#     if number_of_shots == gun_barrel_size and bullets:
#         print("Reloading!")
#         number_of_shots = 0

# if locks:
#     print(f"Couldn't get through. Locks left: {len(locks)}")
# else:
#     print(f"{len(bullets)} bullets left. Earned ${prize_of_the_value}")
