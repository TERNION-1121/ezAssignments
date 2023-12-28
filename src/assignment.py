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
        
            num, question_type = question[0].split('.') 
            num = int(num)
            question_type = question_type.strip()

            match question_type:
                case "MCQ":
                    self.MCQS.append(MCQ(question[1], question[2:6], num))
                case "AR":
                    # find index of element starting with "R:"
                    for i in range(len(question)):
                        if question[i].startswith('R:'):
                            self.ARS.append(AR(question[1:i], question[i:], num))
                            break
                case "OBJ":
                    self.OBJS.append(OBJ(question[1:], num)) 
                case "SUB":
                    self.SUBS.append(SUB(question[1:], num))