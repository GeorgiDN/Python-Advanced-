from collections import deque
worms = list(map(int, input().split(" ")))
holes = deque(map(int, input().split(" ")))
matches_count = 0
worm_not_fit = False


while worms and holes:
    worm = worms[-1]
    if worm <= 0:
        worms.pop()
        continue
    hole = holes.popleft()
    if worm == hole:
        matches_count += 1
        worms.pop()
    else:
        worm_not_fit = True
        worms[-1] -= 3

if matches_count > 0:
    print(f"Matches: {matches_count}")
else:
    print("There are no matches.")

if not worms:
    if not worm_not_fit:
        print("Every worm found a suitable hole!")
    elif worm_not_fit:
        print("Worms left: none")
else:
    print(f"Worms left: {', '.join(map(str, worms))}")

if not holes:
    print("Holes left: none")
else:
    print(f"Holes left: {', '.join(map(str, holes))}")
  
