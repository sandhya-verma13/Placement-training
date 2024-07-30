from itertools import permutations
n=input().split()
s=''.join(sorted(n[0]))
b=permutations(s,int(n[1]))
for s in b:
    print(''.join(s))
