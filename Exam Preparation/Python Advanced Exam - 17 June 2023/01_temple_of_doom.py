from collections import deque

harry_tools = deque(map(int, input().split(" ")))
substances = list(map(int, input().split(" ")))
challenges = list(map(int, input().split(" ")))


while harry_tools and substances:
    tool = harry_tools.popleft()
    curr_substance = substances.pop()
    result = tool * curr_substance
    if result in challenges:
        challenges.remove(result)
    else:
        harry_tools.append(tool+1)
        curr_substance -= 1
        if curr_substance >= 1:
            substances.append(curr_substance)

if len(challenges) == 0:
    print(f"Harry found an ostracon, which is dated to the 6th century BCE.")

elif len(challenges) > 0:
    print("Harry is lost in the temple. Oblivion awaits him.")

if harry_tools:
    print(f"Tools: {', '.join(map(str, harry_tools))}")
if substances:
    print(f"Substances: {', '.join(map(str, substances))}")
if challenges:
    print(f"Challenges: {', '.join(map(str, challenges))}")
