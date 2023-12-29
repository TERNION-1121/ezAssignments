class OBJ:
    def __init__(self, number: int, question: list[str]) -> None:
        self.number = number
        self.question = question

    def __repr__(self) -> str:
        return f"OBJ({self.number}, {' '.join(self.question)})"
