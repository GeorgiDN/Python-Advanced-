from collections import deque

bullet_price = int(input())
gun_barrel_size = int(input())
bullets = list(map(int, input().split()))       # bullets are a stack
locks = deque(list(map(int, input().split())))  # locks are a queue
prize_value = int(input())
shots = 0

while bullets:
    if len(locks) == 0:
        break
    shots += 1
    current_bullet = bullets.pop()
    prize_value -= bullet_price
    if current_bullet <= locks[0]:
        print("Bang!")
        locks.popleft()
    else:
        print("Ping!")
    if shots == gun_barrel_size and bullets:
        print("Reloading!")
        shots = 0

if locks:
    print(f"Couldn't get through. Locks left: {len(locks)}")
else:
    print(f"{len(bullets)} bullets left. Earned ${prize_value}")
    
