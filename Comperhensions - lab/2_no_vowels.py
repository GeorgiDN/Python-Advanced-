vowels = ['a', 'o', 'u', 'e', 'i']
# res = [char for char in input() if char.lower() not in vowels]
res = [char for char in input() if char.casefold() not in vowels]
print(''.join(res))
