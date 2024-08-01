from itertools import groupby
a=input().strip()
s=groupby(a)
result = ' '.join(f"({len(list(group))}, {key})" for key, group in s)
print(result)
        
