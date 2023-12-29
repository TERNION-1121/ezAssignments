from src.question_classes import *
from src.utils.utils import Utilities

class Assignment:
    def __init__(self, path: str) -> None:

        file = open(path)
        contents = [line.rstrip('\n').strip() if line != '\n' else '\n' for line in file]
        file.close()

        contents = Utilities.split_list(contents, '\n')

        self.MCQS = []
        self.ARS  = []
        self.OBJS = []
        self.SUBS = []

        for question in contents:
            self.validQuestion(question)

        self.MCQS = filter(lambda x: x, self.MCQS)
        self.ARS  = filter(lambda x: x, self.ARS)
        self.OBJS = filter(lambda x: x, self.OBJS)
        self.SUBS = filter(lambda x: x, self.SUBS)
    
       
    def validQuestion(self, question_content: list[str]):
        num, question_type = map(str.strip, question_content[0].split('.'))
    
        try:
            num = int(num)
        except:
            return 
        
        match question_type:
            case 'MCQ':
                self.MCQS.append(MCQ.fromList(num, question_content[1:]))
            case 'AR':
                self.ARS.append(AR.fromList(num, question_content[1:]))
            case 'OBJ':
                self.OBJS.append(OBJ.fromList(num, question_content[1:]))
            case 'SUB':
                self.SUBS.append(SUB.fromList(num, question_content[1:]))