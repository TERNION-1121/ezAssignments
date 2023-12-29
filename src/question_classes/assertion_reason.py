from src.utils.utilities import Utilities

class AR:
    OPTIONS = { 'A.': "Both Assertion and Reason are True, and Reason is the correct explanation for Assertion",
                'B.': "Both Assertion and Reason are True, but Reason is not the correct explanation for Assertion",
                'C.': "Assertion is True, Reason is False",
                'D.': "Assertion is False, Reason is True",
                'E.': "Both Assertion and Reason are False"
            }
    def __init__(self, number: int, assertion: list[str], reason: list[str]) -> None:
        self.number = number
        self.assertion = assertion
        self.reason = reason 
    
    @classmethod
    def fromList(cls, number, question_content: list[str]):
        # ['A: <assertion>', '<assertion_line_2>', 'R: <reason>', '<reason_line_2>']
        index = Utilities.elementStartsWith(question_content, "R:")
        return cls(number, question_content[:index], question_content[index:])

    def __repr__(self) -> str:
        return f"AR({self.number}, {' '.join(self.assertion)}, {' '.join(self.reason)})"