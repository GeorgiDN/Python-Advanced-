from collections import deque

food_packages = list(map(int, input().split()))
food_requests = deque(map(int, input().split()))
target = int(input())
collected_points = 0

while food_packages and food_requests:
    food = food_packages.pop()
    requests = food_requests.popleft()

    if food == requests:
        collected_points += 1

    elif food > requests:
        collected_points += 1
        food -= requests
        food -= 1

        if food > 0:
            if food_packages:
                food_packages[-1] += food
            else:
                food_packages.append(food)

    else:
        requests -= food
        food_requests.append(requests)

if collected_points >= target:
    print(f"Food relief success! Daniel helped {collected_points} charity points.")
elif collected_points > 0:
    print(f"Daniel made a difference! He helped {collected_points} charity points.")
else:
    print("Daniel could not help much this time. He will try again next week.")

if food_packages:
    print("Remaining food packages:", '; '.join(map(str, reversed(food_packages))))
if food_requests:
    print("Unmet food requests:", '; '.join(map(str, food_requests)))
