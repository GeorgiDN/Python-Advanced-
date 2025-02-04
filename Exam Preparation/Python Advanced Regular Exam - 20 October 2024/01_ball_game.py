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


strength_values = list(map(int, input().split()))
accuracy_values = deque(map(int, input().split()))
scored_goals = 0

while strength_values and accuracy_values:
    strength = strength_values.pop()
    accuracy = accuracy_values.popleft()

    result = strength + accuracy

    if result == 100:
        scored_goals += 1

    elif result < 100:
        if strength < accuracy:
            accuracy_values.appendleft(accuracy)
        elif strength > accuracy:
            strength_values.append(strength)
        else:
            strength_values.append(result)

    elif result > 100:
        strength -= 10
        strength_values.append(strength)
        accuracy_values.append(accuracy)

print(get_message(scored_goals))
if scored_goals > 0:
    print(f"Goals scored: {scored_goals}")
if strength_values:
    print(f"Strength values left: {', '.join(map(str, strength_values))}")
if accuracy_values:
    print(f"Accuracy values left: {', '.join(map(str, accuracy_values))}")
