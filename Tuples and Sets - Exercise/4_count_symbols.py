from collections import Counter

text = input()
[print(f'{letter}: {count} time/s') for letter, count in sorted(Counter(text).items())]


# from collections import Counter
# [print(f'{letter}: {count} time/s') for letter, count in sorted(Counter(input()).items())]



# from collections import defaultdict
#
# characters_data = defaultdict(int)
# text = input()
# for char in text:
#     characters_data[char] += 1
# [print(f'{letter}: {count} time/s') for letter, count in sorted(characters_data.items())]



# from collections import Counter

# text = input()
# occurrences = Counter(text)
# sorted_occurrences = dict(sorted(occurrences.items()))
# print("\n".join([f"{char}: {count} time/s" for char, count in sorted_occurrences.items()]))
