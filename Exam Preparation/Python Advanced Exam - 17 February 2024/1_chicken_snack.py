# https://judge.softuni.org/Contests/Practice/Index/4527#0
from collections import deque

henry_money = list(map(int, input().split()))
food_prices = deque(map(int, input().split()))
eaten_foods = 0


while henry_money and food_prices:
    money = henry_money[-1]
    price = food_prices.popleft()

    if money == price:
        eaten_foods += 1
        henry_money.pop()

    elif money < price:
        henry_money.pop()

    else:
        change = money - price
        henry_money.pop()
        eaten_foods += 1
        if henry_money:
            henry_money[-1] += change
        else:
            henry_money.append(change)

if eaten_foods >= 4:
    print(f"Gluttony of the day! Henry ate {eaten_foods} foods.")
elif 1 < eaten_foods < 4:
    print(f"Henry ate: {eaten_foods} foods.")
elif eaten_foods == 1:
    print(f"Henry ate: {eaten_foods} food.")
else:
    print("Henry remained hungry. He will try next weekend again.")
