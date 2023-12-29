class MCQ:
    def __init__(self, number: int, question: str, options: dict[str:str]) -> None:
        self.number = number 
        self.question = question
        self.options = options
    
    @classmethod
    def fromList(cls, number, question_content: list[str]):
        # ['<question>', '<opt A>', '<opt B>', '<opt C>', '<opt D>']
        options = question_content[1:]
        options = {chr(65+i):options[i] for i in range(4)}

        return cls(number, question_content[0], options)
        
    def __repr__(self) -> str:
        return f"MCQ({self.number}, {self.question}, {self.options})"