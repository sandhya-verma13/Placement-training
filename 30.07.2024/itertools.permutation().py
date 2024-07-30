from itertools import permutations
m=input().split()
k=''.join(sorted(m[0]))
l=permutations(k,int(m[1]))
for k in l:
    print(''.join(k))
