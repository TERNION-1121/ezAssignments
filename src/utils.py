class Utilities:
    @staticmethod
    def split_list(lst: list) -> list[list]:
        s = 0
        splitted = []

        for e in range(len(lst)):
            if lst[e] == '\n':
                splitted.append(lst[s:e])
                s = e + 1

        return splitted + lst[s:]