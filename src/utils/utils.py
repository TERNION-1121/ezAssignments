class Utilities:
    @staticmethod
    def split_list(lst: list, delimiter: str) -> list[list]:
        s = 0
        splitted = []

        for e in range(len(lst)):
            if lst[e] == delimiter:
                splitted.append(lst[s:e])
                s = e + 1
        splitted.append(lst[s:])
        return splitted
    
    @staticmethod
    def isValidQuestion(question: list[str]) -> bool:
        pass