from docx import Document


class Question:
    QUESTIONS = list()
    INSTRUCTIONS = None

    def __init__(self, question: list[str] | None = None) -> None:
        self.question = question
        # add to class attribute QUESTIONS
        self.QUESTIONS.append(self)

    @classmethod
    def process_instructions(cls) -> None:
        """
        Ask the user to process optional instructions in the main program
        """
        yes_opts = ('y', 'yes')
        no_opts = ('n', 'no')
        # ask choice
        print(f"Add instructions for {cls.__name__}? (y/n):", end=" ")
        while (choice := input().strip().lower()) not in yes_opts + no_opts:
            print("\033[1A\033[0J", end='')
            print(f"Add instructions for {cls.__name__}? (y/n):", end=" ")
        # quit if user denies for any instruction
        if choice in no_opts:
            cls.INSTRUCTIONS = None
            return
        # ask to use default instructions, if any
        if cls.INSTRUCTIONS is not None:
            print(f"Default instructions for {cls.__name__}:")
            print(''.join(cls.INSTRUCTIONS))

            print("Continue with default instructions? (y/n):", end=" ")
            while (choice := input().strip().lower()) not in yes_opts + no_opts:
                print("\033[1A\033[0J", end='')
                print("Continue with default instructions? (y/n):", end=" ")

            if choice in yes_opts:
                print()
                return
        # ask user's own instructions
        print("Write your instructions (enter a blank newline to stop giving input):")
        cls.INSTRUCTIONS = list()
        while inp := input().strip():
            cls.INSTRUCTIONS.append(f"{inp}\n")

    @classmethod
    def write_instructions(cls, doc: Document) -> None:
        if not cls.INSTRUCTIONS:
            return

        instruction = doc.add_paragraph()
        for line in cls.INSTRUCTIONS:
            instruction.add_run(line)


class Invalid:
    QUESTIONS = list()

    def __init__(self, question: list[str] | None = None) -> None:
        self.statement = [line + '\n' for line in question]

        Invalid.QUESTIONS.append(self)


class MCQ(Question):
    QUESTIONS = list()
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
    def write_instructions(cls, doc: Document) -> None:
        super(MCQ, cls).write_instructions(doc)

    @classmethod
    def from_list_content(cls, content: list[str]):
        question = []
        # stores the question statement
        for line in content:
            if line == '\n':
                break
            question.append(line)
        else:  # no newline was encountered to distinguish question statement from options
            return None
        # store options
        opt_statements = content[-4:]
        if len(opt_statements) != 4:  # correct number of options were not supplied
            return None
        # TODO: check for empty lines in opt_statements
        options = dict(zip(['A', 'B', 'C', 'D'], opt_statements))

        return cls(question, options)

    def __repr__(self) -> str:
        return f"""MCQ({self.question[0][:10]}...{self.question[-1][-10:]})"""


class AR(Question):
    QUESTIONS = list()
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
        super().__init__()
        self.assertion = assertion
        self.reason = reason

    @classmethod
    def process_instructions(cls) -> None:
        super(AR, cls).process_instructions()

    @classmethod
    def write_instructions(cls, doc: Document) -> None:
        super(AR, cls).write_instructions(doc)

    @classmethod
    def from_list_content(cls, content: list[str]):
        try:
            sep_index = content.index('\n')
        except ValueError:  # no newline was found to distinguish assertion from reasoning statement
            return None

        assertion = content[:sep_index]
        reason = content[sep_index + 1:]

        return cls(assertion, reason)

    def __repr__(self) -> str:
        return f"""AR(A:{self.assertion[0][:10]}...R:{self.reason[0][:10]})"""


class SUB(Question):
    QUESTIONS = list()
    INSTRUCTIONS = None

    def __init__(self, question: list[str]) -> None:
        super().__init__(question)

    @classmethod
    def process_instructions(cls) -> None:
        super(SUB, cls).process_instructions()

    @classmethod
    def write_instructions(cls, doc: Document) -> None:
        super(SUB, cls).write_instructions(doc)

    @classmethod
    def from_list_content(cls, content: list[str]):
        return cls(content)

    def __repr__(self) -> str:
        return f"""SUB({self.question[0][:10]}...{self.question[-1][-10:]})"""
