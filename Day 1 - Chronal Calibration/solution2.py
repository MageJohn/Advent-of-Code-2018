with open("input.txt") as input1:
    changes = input1.readlines()
    changes = [int(line) for line in changes]

freqs = set()
total = 0
i = 0
while total not in freqs:
    freqs.add(total)
    total += changes[i]
    i = (i + 1) % len(changes)

print(total)
