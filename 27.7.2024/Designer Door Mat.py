def print_door_mat(rows, cols):
    pattern = ".|."  # Pattern for the design
    welcome_message = "WELCOME"
    for i in range(rows // 2):
        pattern_width = (i * 2 + 1) * len(pattern)  # Width of the pattern in the current row
        padding = (cols - pattern_width) // 2  # Calculate the padding on both sides
        print("-" * padding + pattern * (i * 2 + 1) + "-" * padding)
    welcome_padding = (cols - len(welcome_message)) // 2
    print("-" * welcome_padding + welcome_message + "-" * welcome_padding)
    for i in range(rows // 2 - 1, -1, -1):
        pattern_width = (i * 2 + 1) * len(pattern)  # Width of the pattern in the current row
        padding = (cols - pattern_width) // 2  # Calculate the padding on both sides
        print("-" * padding + pattern * (i * 2 + 1) + "-" * padding)
rows, cols = map(int, input().split())
print_door_mat(rows, cols)
