from collections import Counter


def can_be_poly(line: str) -> bool:
    return len(line) % 2 == sum(x % 2 for x in Counter(line).values())


print(can_be_poly('abcba'))  # Counter({'a': 2, 'b': 2, 'c': 2})
print(can_be_poly('abbbc'))  # Counter({'b': 3, 'c': 2, 'a': 1})
