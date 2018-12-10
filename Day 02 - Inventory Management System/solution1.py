from collections import Counter

with open("input.txt") as ids:
    ids = ids.readlines()

twice = 0
thrice = 0
for ID in ids:
    charfreq = Counter(ID)
    if 2 in charfreq.values():
        twice += 1
    if 3 in charfreq.values():
        thrice += 1

print(twice * thrice)
