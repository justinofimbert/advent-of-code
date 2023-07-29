def get_ending_floor(parentheses: str) -> int:
    position = 0
    for char in parentheses:
        if char == "(":
            position += 1
        elif char == ")":
            position -= 1

    return position


if __name__ == "__main__":
    print(
        get_ending_floor(
            input("please enter the sequence of parentheses here and hit return.")
        )
    )
