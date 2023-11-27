number = int(input())
unique_names = [input() for _ in range(number)]
set_unique_names = set(unique_names)

for name in set_unique_names:
    print(name)
  
