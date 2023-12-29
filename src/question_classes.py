class Question:
    def __init__(self, number: int, question: str) -> None:
        self.number = number
        self.question = question

class MCQ(Question):
    def __init__(self, number: int, question: str, options: dict[str:str]) -> None:
        super().__init__(number, question)
        self.options = options
    
    @classmethod
    def fromList(cls, number, question_content: list[str]):
        # ['1. MCQ', '<question>', '<question_line_2>', 'A. <opt A>', 'B. <opt B>', 'C. <opt C>', 'D. <opt D>']
        pass
        
    def __repr__(self) -> str:
        pass

class AR:
    def __init__(self, assertion: str, number: int, reason: str) -> None:
        self.number = number
        self.assertion = assertion
        self.reason = reason 
    
    @classmethod
    def fromList(cls, number, question_content: list[str]):
        # ['2. AR', 'A: <assertion>', '<assertion_line_2>', 'R: <reason>', '<reason_line_2>'],
        pass

    def __repr__(self) -> str:
        pass

class OBJ(Question):
    def __init__(self, number: int, question: str) -> None:
        super().__init__(number, question)

    @classmethod
    def fromList(cls, number, question_content: list[str]):
        # ['3. OBJ', '<question>', '<question_line_2>']
        pass

    def __repr__(self) -> str:
        pass

class SUB(Question):
    def __init__(self, number: int, question: str) -> None:
        super().__init__(number, question)

    @classmethod
    def fromList(cls, number, question_content: list[str]):
        # ['4. SUB', '<question>', '<question_line_2']
        pass

    def __repr__(self) -> str:
        pass