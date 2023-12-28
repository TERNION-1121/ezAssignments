from src.question_classes import *
from src.utils import Utilities

class Assignment:
    def __init__(self, path: str) -> None:
        with open(path) as file:
            contents = [line.rstrip('\n').strip() if line != '\n' else '\n' for line in file]
        contents = Utilities.split_list(contents)
        
        for question in contents:
            if question[0].endswith("MCQ"):
                pass
            if question[0].endswith("AR"):
                pass
            if question[0].endswith("OBJ"):
                pass 
            if question[0].endswith("SUB"):
                pass