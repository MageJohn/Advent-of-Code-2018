with open("input.txt") as ids:
    ids = [ID.strip() for ID in ids.readlines()]


def match(s1, s2):
    diff_i = None
    for i, (c1, c2) in enumerate(zip(s1, s2)):
        if c1 != c2:
            if diff_i:
                return False
            else:
                diff_i = i
    return diff_i


result = None
for id1 in ids:
    for id2 in ids:
        diff_i = match(id1, id2)
        if diff_i:
            result = id1[:diff_i] + id1[diff_i+1:]
            break
    if result:
        break

print(result)
