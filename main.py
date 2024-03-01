from src.assignment import Assignment

def main():
    assignment = Assignment("assignment.txt")
    assignment.InitDoc()

    if assignment.QUESTIONS["MCQS"]:
        assignment.AddMCQS()
    if assignment.QUESTIONS["ARS"]:
        assignment.AddARS()
    if assignment.QUESTIONS["SUBS"]:
        assignment.AddSUBS()

    if not assignment.QUESTIONS["INVALIDATED"]:
        return 
    
    with open("invalidated_questions.txt", 'w') as file:
        file.write("THE FOLLOWING QUESTIONS WERE INVALIDATED:\n\n")
        for question in assignment.QUESTIONS["INVALIDATED"]:
            for line in question:
                file.write(line + '\n')
            file.write('\n')

if __name__ == "__main__":
    main()