import re
email = input().strip()
if '@' not in email:
    print("invalid input")
else:
    local_part, domain_part = email.split('@', 1)
    if not (15 <= len(email) <= 35):
        print("NO")
    elif domain_part != "redtape.com":
        print("NO")
    else:
        if not re.match(r'^[a-z]', local_part):
            print("NO")
        elif not re.search(r'[a-zA-Z]', local_part) or not re.search(r'\d', local_part):
            print("NO")
        else:
            special_char_count = sum(c in '#$' for c in local_part)
            if special_char_count != 1:
                print("NO")
            else:
                print("YES")
