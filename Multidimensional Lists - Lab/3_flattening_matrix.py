rows = int(input())
matrix = [int(x) for _ in range(rows) for x in input().split(", ")]
print(matrix)



# rows = int(input())
# print([int(x) for _ in range(rows) for x in input().split(", ")])



# print([int(x) for _ in range(int(input())) for x in input().split(", ")])



# rows = int(input())
# matrix = []
# 
# for _ in range(rows):
#     numbers = [int(x) for x in input().split(", ")]
#     matrix.extend(numbers)
# 
# print(matrix)
