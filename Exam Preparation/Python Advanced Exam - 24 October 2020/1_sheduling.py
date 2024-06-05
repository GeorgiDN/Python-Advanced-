import sys

jobs = list(map(int, input().split(', ')))
searched_index = int(input())
cycles = 0
max_number = sys.maxsize

while True:
    index = jobs.index(min(jobs))
    if index == searched_index:
        cycles += jobs[index]
        break
    cycles += jobs[index]
    jobs[index] = max_number

print(cycles)




# jobs = list(map(int, input().split(', ')))
# searched_index = int(input())
# 
# indexed_jobs = list(enumerate(jobs))
# indexed_jobs.sort(key=lambda x: x[1])
# 
# cycles = 0
# 
# for index, job in indexed_jobs:
#     cycles += job
#     if index == searched_index:
#         break
# 
# print(cycles)
