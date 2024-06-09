# #https://judge.softuni.org/Contests/Practice/Index/4089#0

from collections import deque

monsters = deque(map(int, input().split(',')))
soldiers = list(map(int, input().split(',')))
monsters_killed = 0

while monsters and soldiers:
    monster = monsters.popleft()
    strike = soldiers.pop()

    if strike >= monster:
        strike -= monster
        monsters_killed += 1
        if strike > 0:
            if not soldiers:
                soldiers.append(strike)
            else:
                soldiers[-1] += strike
    else:
        monster -= strike
        monsters.append(monster)

if not monsters:
    print("All monsters have been killed!")
if not soldiers:
    print("The soldier has been defeated.")
print(f"Total monsters killed: {monsters_killed}")
