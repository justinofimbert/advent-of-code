class Santa:
    def __init__(self, location: tuple = (0, 0)) -> None:
        if len(location) != 2:
            raise ValueError("tuple size must be equal to two.")

        if not isinstance(location[0], int) or not isinstance(location[1], int):
            raise ValueError("values of location have to be integers.")

        self.location = location
        self.path: list = [location]

    def move(self, direction: str) -> None:
        if direction not in "^>v<":
            return None

        if direction == "^":
            self.location = (self.location[0], self.location[1] + 1)

        elif direction == ">":
            self.location = (self.location[0] + 1, self.location[1])

        elif direction == "v":
            self.location = (self.location[0], self.location[1] - 1)

        elif direction == "<":
            self.location = (self.location[0] - 1, self.location[1])

        self.path.append(self.location)

    def path(self) -> list:
        return self.path


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        directions = file.read()

    santa = Santa()
    santas = [Santa(), Santa()]
    for direction_number, direction in enumerate(directions):
        santa.move(direction)

        if direction_number % 2 == 0:
            santas[0].move(direction)

        else:
            santas[1].move(direction)

    houses_visited_by_santa = len(set(santa.path))
    print(f"houses visited by Santa: {houses_visited_by_santa}")

    houses_visited_by_two_santas = len(
        set([house for santa in santas for house in santa.path])
    )
    print(f"houses visited by Santa and Robo-Santa: {houses_visited_by_two_santas}")
