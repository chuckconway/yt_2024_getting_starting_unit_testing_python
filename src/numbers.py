class Numbers:
    def __init__(self, left: int, right: int):
        self.left = left
        self.right = right


def add_numbers(numbers: Numbers) -> int:
    return numbers.left + numbers.right