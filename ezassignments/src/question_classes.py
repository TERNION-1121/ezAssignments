import docx


class Question:
    INSTRUCTIONS = None

    def __init__(self, question: list[str] | None) -> None:
        self.question = question

    @classmethod
    def process_instructions(cls) -> None:
        """
        Prompt the user to process optional instructions in the main program
        """
        yes_opts = ('y', 'yes')
        no_opts = ('n', 'no')
        choice = None

        while choice not in yes_opts + no_opts:
            print(f"Add instructions for {cls.__name__}? (y/n):", end=" ")
            choice = input().strip().lower()

        if choice in no_opts:
            cls.INSTRUCTIONS = None
            return

        if cls.INSTRUCTIONS is not None:
            print(f"Default instructions for {cls.__name__}:")
            print(''.join(cls.INSTRUCTIONS))

            choice = None
            while choice not in yes_opts + no_opts:
                print("Continue with default instructions? (y/n):", end=" ")
                choice = input().strip().lower()

            if choice in yes_opts:
                return

        print("Write your instructions (enter a blank newline to stop giving input):")
        cls.INSTRUCTIONS = list()
        while inp := input().strip():
            cls.INSTRUCTIONS.append(f"{inp}\n")

    @classmethod
    def write_instructions(cls, doc: docx.Document) -> None:
        if not cls.INSTRUCTIONS:
            return

        instruction = doc.add_paragraph()
        for line in cls.INSTRUCTIONS:
            instruction.add_run(line)


class MCQ(Question):
    INSTRUCTIONS = None

    def __init__(self,
                 question: list[str],
                 options: dict[str:str]) -> None:
        super().__init__(question)
        self.options = options

    @classmethod
    def process_instructions(cls) -> None:
        super(MCQ, cls).process_instructions()

    @classmethod
    def write_instructions(cls, doc: docx.Document) -> None:
        super(MCQ, cls).write_instructions(doc)

    @classmethod
    def from_list_content(cls, content: list[str]):
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


class AR(Question):
    INSTRUCTIONS = ["The following questions consist of two statements- Assertion (A) and Reasoning (R)\n",
                    "Answer these questions selecting the most appropriate option given below:"]
    OPTIONS = {'A': "Both Assertion (A) and Reason (R) are True, and R is the correct explanation of A.",
               'B': "Both Assertion (A) and Reason (R) are True, but R is not the correct explanation of A.",
               'C': "Assertion (A) is True, Reason (R) is False.",
               'D': "Assertion (A) is False, Reason (R) is True",
               'E': "Both Assertion (A) and Reason (R) are False"
               }

    def __init__(self,
                 assertion: list[str],
                 reason: list[str]) -> None:
        super().__init__(None)
        self.assertion = assertion
        self.reason = reason

    @classmethod
    def process_instructions(cls) -> None:
        super(AR, cls).process_instructions()

    @classmethod
    def write_instructions(cls, doc: docx.Document) -> None:
        super(AR, cls).write_instructions(doc)

    @classmethod
    def from_list_content(cls, content: list[str]):
        try:
            sep_index = content.index('\n')
        except ValueError:
            return None

        assertion = content[:sep_index]
        reason = content[sep_index + 1:]

        return cls(assertion, reason)

    def __repr__(self) -> str:
        return f"""AR(A:{self.assertion[0][:10]}...R:{self.reason[0][:10]})"""


class SUB(Question):
    INSTRUCTIONS = None

    def __init__(self, question: list[str]) -> None:
        super().__init__(question)

    @classmethod
    def process_instructions(cls) -> None:
        super(SUB, cls).process_instructions()

    @classmethod
    def write_instructions(cls, doc: docx.Document) -> None:
        super(SUB, cls).write_instructions(doc)

    def __repr__(self) -> str:
        return f"""SUB({self.question[0][:10]}...{self.question[-1][-10:]})"""
