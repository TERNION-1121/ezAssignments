def split_contents(contents: list) -> list[list[str]]:
    s = 0
    splitted_contents = []

    for e in range(len(contents) - 1):
        if contents[e] == '\n' and contents[e+1] == '\n':
            splitted_contents.append(contents[s:e])
            s = e + 2
    splitted_contents.append(contents[s:])
    return splitted_contents