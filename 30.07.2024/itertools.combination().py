from itertools import combinations
m=input().split()
k=''.join(sorted(m[0]))
for i in range(0,int(m[1])):
    l=combinations(k,i+1)
    for j in l:
        print(''.join(j))
