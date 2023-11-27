n = int(input())

unique = set()
for i in range(n):
    chemical_compounds = input().split(' ')
    for chem in chemical_compounds:
        unique.add(chem)

for char in unique:
    print(char)
  
