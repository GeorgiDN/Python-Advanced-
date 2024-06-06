from collections import deque

duck_times = {
    range(0, 61): 'Darth Vader Ducky',
    range(61, 121): 'Thor Ducky',
    range(121, 181): 'Big Blue Rubber Ducky',
    range(181, 241): 'Small Yellow Rubber Ducky'
}

duck_manufactured = {'Darth Vader Ducky': 0,
                     'Thor Ducky': 0,
                     'Big Blue Rubber Ducky': 0,
                     'Small Yellow Rubber Ducky': 0}

programmers_time = deque(map(int, input().split()))
task_numbers = list(map(int, input().split()))

while programmers_time and task_numbers:
    p_time = programmers_time.popleft()
    task = task_numbers.pop()

    need_time = p_time * task
    duck_found = False
    for time_range, duck_type in duck_times.items():
        if need_time in time_range:
            duck_manufactured[duck_type] += 1
            duck_found = True
            break

    if not duck_found:
        programmers_time.append(p_time)
        task_numbers.append(task - 2)

print("Congratulations, all tasks have been completed! Rubber ducks rewarded:")
for d, count in duck_manufactured.items():
    print(f"{d}: {count}")

