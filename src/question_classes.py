class Question:
    def __init__(self, question: list[str]) -> None:
        self.question = question


class MCQ(Question):
    def __init__(self, question: list[str], options: dict[str:str]) -> None:
        super().__init__(question)
        self.options = options
    
    @classmethod
    def FromListContent(cls, content: list[str]):
        question = []   
        # stores the question statement
        for line in content:
            if line == '\n':
                break 
            question.append(line)
        # store options
        options = dict(zip(['A', 'B', 'C', 'D'], content[-4:]))
        
        return cls(question, options)

    def __repr__(self) -> str:
        return f"""MCQ({self.question[0][:10]}...{self.question[-1][-10:]})"""


class AR:
    OPTIONS = { 'A': "Both Assertion (A) and Reason (R) are True, and R is the correct explanation of A.",
                'B': "Both Assertion (A) and Reason (R) are True, but R is not the correct explanation of A.",
                'C': "Assertion (A) is True, Reason (R) is False.",
                'D': "Assertion (A) is False, Reason (R) is True",
                'E': "Both Assertion (A) and Reason (R) are False"
                }
    
    def __init__(self, assertion: list[str], reason: list[str]) -> None:
        self.assertion = assertion
        self.reason = reason 
    
    @classmethod
    def FromListContent(cls, content: list[str]):
        assertion = []
        reason = []

        try:
            sep_index = content.index('\n')
        except ValueError: 
            return None

        assertion = content[:sep_index]
        reason = content[sep_index+1:]

        return cls(assertion, reason)

    def __repr__(self) -> str:
        return f"""AR(A:{self.assertion[0][:10]}...R:{self.reason[0][:10]})"""


class SUB(Question):
    def __init__(self, question: list[str]) -> None:
        super().__init__(question)
    
    def __repr__(self) -> str:
        return f"""SUB({self.question[0][:10]}...{self.question[-1][-10:]})"""