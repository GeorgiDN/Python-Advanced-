#https://judge.softuni.org/Contests/Practice/Index/4089#0

from collections import deque

armour_values = deque(map(int, input().split(",")))
soldier_strike_impacts = list(map(int, input().split(",")))
monster_killed = 0

while armour_values and soldier_strike_impacts:
    monster_armour = armour_values.popleft()
    soldier_strike = soldier_strike_impacts.pop()
    if soldier_strike == monster_armour:
        monster_killed += 1
    elif soldier_strike > monster_armour:
        monster_killed += 1
        rest_impact = soldier_strike - monster_armour
        if len(soldier_strike_impacts) > 0:
            soldier_strike_impacts[-1] += rest_impact
        elif not soldier_strike_impacts and rest_impact > 0:
            soldier_strike_impacts.append(rest_impact)
    elif soldier_strike < monster_armour:
        monster_armour -= soldier_strike
        armour_values.append(monster_armour)


if not armour_values:
    print("All monsters have been killed!")
if not soldier_strike_impacts:
    print("The soldier has been defeated.")

print(f"Total monsters killed: {monster_killed}")
