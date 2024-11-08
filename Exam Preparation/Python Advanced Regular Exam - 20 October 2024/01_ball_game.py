from collections import deque


def get_message(goals):
    conditions = {
        3: "Paul scored a hat-trick!",
        0: "Paul failed to score a single goal.",
        (4, float('inf')): "Paul performed remarkably well!",
        (1, 3): "Paul failed to make a hat-trick.",
    }

    if goals in conditions:
        return conditions[goals]

    for key, message in conditions.items():
        if isinstance(key, tuple):
            start, end = key
            if start <= goals < end:
                return message


required_strength = list(map(int, input().split()))
needed_accuracy = deque(map(int, input().split()))
total_goals = 0

while required_strength and needed_accuracy:
    strength = required_strength.pop()
    accuracy = needed_accuracy.popleft()

    if strength + accuracy == 100:
        total_goals += 1

    elif strength + accuracy < 100:
        if strength < accuracy:
            needed_accuracy.appendleft(accuracy)
        elif strength > accuracy:
            required_strength.append(strength)
        else:
            result = strength + accuracy
            required_strength.append(result)

    else:
        strength -= 10
        required_strength.append(strength)
        needed_accuracy.append(accuracy)

print(get_message(total_goals))
if total_goals > 0:
    print(f"Goals scored: {total_goals}")

if required_strength:
    print(f"Strength values left: {', '.join(map(str, required_strength))}")
if needed_accuracy:
    print(f"Accuracy values left: {', '.join(map(str, needed_accuracy))}")
