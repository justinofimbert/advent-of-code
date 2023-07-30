class Santa:
    def __init__(self, location: tuple = (0, 0)) -> None:
        self.location = location
        self.path = [location]

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
    for direction in directions:
        santa.move(direction)

    houses_visited_by_santa = len(set(santa.path))

    print(f"houses visited by santa: {houses_visited_by_santa}")
