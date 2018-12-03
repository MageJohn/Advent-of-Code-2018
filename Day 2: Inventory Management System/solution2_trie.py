with open('testinput.txt') as ids:
    ids = ids.readlines()
    ids = [s.strip() for s in ids]


def build_trie(s, trie):
    if len(s) == 0:
        return
    if s[0] not in trie:
        trie[s[0]] = {}
    build_trie(s[1:], trie[s[0]])


trie = {}
for ID in ids:
    build_trie(ID, trie)


