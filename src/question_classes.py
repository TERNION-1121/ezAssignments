class Question:
    def __init__(self, question: str, number: int) -> None:
        self.question = question
        self.number = number

    def __repr__(self) -> str:
        return f"Question({self.question}, {self.number})"

class MCQ(Question):
    def __init__(self, question: str, options: list[str], number: int) -> None:
        super().__init__(question, number)
        self.options = {chr(65+i):options[i] for i in range(4)}
        
    def __repr__(self) -> str:
        return f"MCQ({self.question}, {self.options}, {self.number})"

class AR:
    def __init__(self, assertion: str, reason: str, number: int) -> None:
        self.number = number
        self.assertion = assertion
        self.reason = reason 
    
    def __repr__(self) -> str:
        pass

class OBJ(Question):
    def __init__(self, question: str, number: int) -> None:
        super().__init__(question, number)

    def __repr__(self) -> str:
        pass

class SUB(Question):
    def __init__(self, question: str, number: int) -> None:
        super().__init__(question, number)

    def __repr__(self) -> str:
        pass