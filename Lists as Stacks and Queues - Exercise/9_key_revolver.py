from collections import deque

bullet_price = int(input())
gun_barrel_size = int(input())
bullets = list(map(int, input().split()))       
locks = deque(list(map(int, input().split()))) 
prize_of_the_value = int(input())
number_of_shots = 0

while bullets:
    if not locks:
        break
    number_of_shots += 1
    bullet = bullets.pop()
    prize_of_the_value -= bullet_price
    if bullet <= locks[0]:
        print("Bang!")
        locks.popleft()
    else:
        print("Ping!")
    if number_of_shots == gun_barrel_size and bullets:
        print("Reloading!")
        number_of_shots = 0

if locks:
    print(f"Couldn't get through. Locks left: {len(locks)}")
else:
    print(f"{len(bullets)} bullets left. Earned ${prize_of_the_value}")
