def print_full_name(first: str, last: str) -> None:
    if len(first) > 10 or len(last) > 10:
        raise ValueError("The length of first and last name should be less than 10.")

    print(f"Hello {first} {last}! You just delved into python.")
