from collections import Counter

text = input()
occurrences = Counter(text)
sorted_occurrences = dict(sorted(occurrences.items()))
print("\n".join([f"{char}: {count} time/s" for char, count in sorted_occurrences.items()]))
