from typing import Union

Numeric = Union[int, float]


class Box:
    def __init__(self, length: Numeric, width: Numeric, height: Numeric) -> None:
        self.length = length
        self.width = width
        self.height = height
        return None

    def compute_sqft_of_wrapping_paper_needed(self) -> Numeric:
        self.UD_faces_surface = self.length * self.width
        self.RL_faces_surface = self.width * self.height
        self.FB_faces_surface = self.length * self.height
        return (
            self.UD_faces_surface * 2
            + self.RL_faces_surface * 2
            + self.FB_faces_surface * 2
            + min(self.UD_faces_surface, self.RL_faces_surface, self.FB_faces_surface)
        )

    def compute_ft_of_ribbon_needed(self) -> Numeric:
        (smallest_dimensions := [self.length, self.width, self.height]).remove( 
            max(smallest_dimensions)
        )
        smallest_perimeter = smallest_dimensions[0] * 2 + smallest_dimensions[1] * 2
        volume = self.length * self.width * self.height
        return smallest_perimeter + volume


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        boxes = file.readlines()

    wrapping_paper_needed_in_sqft = 0
    ribbon_needed_in_ft = 0
    for box in boxes:
        box_dimensions = box.split("x")
        present_box = Box(
            int(box_dimensions[0]), int(box_dimensions[1]), int(box_dimensions[2])
        )
        wrapping_paper_needed_in_sqft += (
            present_box.compute_sqft_of_wrapping_paper_needed()
        )
        ribbon_needed_in_ft += present_box.compute_ft_of_ribbon_needed()

    print(
        f"wrapping paper needed in square feet: {wrapping_paper_needed_in_sqft}.\ntotal ribbon length needed: {ribbon_needed_in_ft}"
    )
