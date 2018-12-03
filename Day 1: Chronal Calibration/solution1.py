with open("input.txt") as input1:
    changes = input1.readlines()
    changes = [int(line) for line in changes]

print(sum(changes))
