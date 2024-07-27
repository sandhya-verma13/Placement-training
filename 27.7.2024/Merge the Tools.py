def merge_the_tools(string, k):
    while string: 
        seen = ''
        s = string[0:k]
        for c in s:
            if c not in seen:
                seen += c
        print(seen)
        string = string[k:]
        
