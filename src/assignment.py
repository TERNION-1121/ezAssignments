from src.question_classes import *
from src.utils import *

class Assignment:

    def __init__(self, path: str) -> None:

        assert path.endswith(".txt"), "File must be of .txt format"
        try:
            file = open(path)
        except FileNotFoundError:
            print(f"File {path} was not found.")
            return
        
        # strip whitespaces from the line if it is not a newline
        contents = [line.strip('\n').strip() if line != '\n' else '\n' for line in file]
        file.close()

        # strip newlines from the start and end of contents
        start = 0
        while contents[start] == '\n':
            start += 1
        
        end = len(contents) - 1
        while contents[end] == '\n':
            end -=1
        
        contents = split_contents(contents[start:end+1])

        self.QUESTIONS = {"MCQS": [], "ARS": [], "SUBS": [], "INVALIDATED": []}

        for question in contents:

            match question[0]:

                case 'MCQ':
                    self.QUESTIONS["MCQS"].append(MCQ.FromListContent(question[1:]))
                case 'AR':
                    self.QUESTIONS["ARS"].append(AR.FromListContent(question[1:]))
                case 'SUB':
                    self.QUESTIONS["SUBS"].append(SUB(question[1:]))
                case _:
                    self.QUESTIONS["INVALIDATED"].append(question)