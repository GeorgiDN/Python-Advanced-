rows = int(input())

unique_chemical_elements = set()
for _ in range(rows):
    elements = input().split()
    for element in elements:
        unique_chemical_elements.add(element)

[print(el) for el in unique_chemical_elements]



# rows = int(input())
#
# all_elements = []
#
# for _ in range(rows):
#     elements = input().split()
#     for element in elements:
#         if element not in all_elements:
#             all_elements.append(element)
#
# [print(el) for el in all_elements]



# rows = int(input())
# print('\n'.join(map(str, {element for _ in range(rows) for element in input().split()})))




# n = int(input())
# 
# unique = set()
# for i in range(n):
#     chemical_compounds = input().split(' ')
#     for chem in chemical_compounds:
#         unique.add(chem)
# 
# for char in unique:
#     print(char)
