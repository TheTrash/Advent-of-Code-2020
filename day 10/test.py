from itertools import combinations
def is_valid(seq):
    return all(n - seq[i] <= 3 for i, n in enumerate(seq[1:]))
    
def count(start, end):
    cnt = 0
    for i in range(end - start):
        comb = list(combinations(f[start + 1:end], i))
        for c in comb:
            to_chk = [f[start]] + list(c) + [f[end]]
            if is_valid(to_chk):
                cnt += 1
    # the anchor generation results in some singletons
    return max(cnt, 1)

f = [0] + sorted((int(n) for n in open('input.txt', 'r').readlines()))
anchors = []
prefix = 0
for i, n in enumerate(f[1:]):
    if n - f[i] == 3:
        anchors.append((prefix, i))
        prefix = i+1
anchors.append((anchors[-1][1], len(f)-1))
perms = 1
for i in anchors:
    perms *= count(*i)
print(perms)