def filter(ls, f):
    return []


ls = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

# Filtering some lists
evens = filter(ls, lambda x: x % 2 == 0)
odds = filter(ls, lambda x: x % 2 != 0)
large = filter(ls, lambda x: x > 5)

print(f"Evens: {evens}")
print(f"Odds: {odds}")
print(f"Greater than 5: {large}")
