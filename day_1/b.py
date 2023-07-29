def get_first_basement_entrance(parentheses: str) -> int:
    position = 0
    movement_count = 1
    for char in parentheses:
        if char == "(":
            position += 1
        elif char == ")":
            position -= 1

        if position == -1:
            return movement_count
        movement_count += 1


if __name__ == "__main__":
    print(
        get_first_basement_entrance(
            input("please enter the sequence of parentheses here and hit return.")
        )
    )
