from src.question_classes import *
from src.utils.utilities import Utilities

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
            self.processQuestion(question)
       
    def processQuestion(self, question_content: list[str]):
        num, question_type = map(str.strip, question_content[0].split('.'))
    
        try:
            num = int(num)
        except:
            return 
        
        # skip question validation
        match question_type:
            case 'MCQ':
                self.MCQS.append(MCQ.fromList(num, question_content[1:]))
            case 'AR':
                self.ARS.append(AR.fromList(num, question_content[1:]))
            case 'OBJ':
                self.OBJS.append(OBJ(num, question_content[1:]))
            case 'SUB':
                self.SUBS.append(SUB(num, question_content[1:]))
    
    def getMCQS(self):
        return str(self.MCQS)
    
    def getARS(self):
        return str(self.ARS)
    
    def getOBJS(self):
        return str(self.OBJS)

    def getSUBS(self):
        return str(self.SUBS)

    def __repr__(self):
        return '\n'.join([self.getMCQS(), self.getARS(), self.getOBJS(), self.getSUBS()])