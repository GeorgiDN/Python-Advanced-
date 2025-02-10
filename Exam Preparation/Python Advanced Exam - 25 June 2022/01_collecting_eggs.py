from collections import deque

eggs = deque(map(int, input().split(', ')))
papers = list(map(int, input().split(', ')))
filled_boxes = 0

while eggs and papers:
    egg = eggs.popleft()
    paper = papers.pop()

    if egg == 13:
        papers.append(paper)
        papers[0], papers[-1] = papers[-1], papers[0]

    elif egg <= 0:
        papers.append(paper)

    elif paper + egg <= 50:
        filled_boxes += 1

if filled_boxes > 0:
    print(f'Great! You filled {filled_boxes} boxes.')
else:
    print(f"Sorry! You couldn't fill any boxes!")

if eggs:
    print(f'Eggs left: {", ".join(map(str, eggs))}')
if papers:
    print(f'Pieces of paper left: {", ".join(map(str, papers))}')
