class Question:
    def __init__(self, question: str, number: int) -> None:
        self.question = question
        self.number = number

class MCQ(Question):
    def __init__(self, question: str, options: dict[str:str], number: int) -> None:
        super().__init__(question, number)
        self.options = options

class AR:
    def __init__(self, assertion: str, reason: str) -> None:
        self.assertion = assertion
        self.reason = reason 

class OBJ(Question):
    def __init__(self, question: str, number: int) -> None:
        super().__init__(question, number)

class SUB(Question):
    def __init__(self, question: str, number: int) -> None:
        super().__init__(question, number)