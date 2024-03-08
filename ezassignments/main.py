from argparse import ArgumentParser
from src import *


def main():
    parser = ArgumentParser(prog="main.py",
                            description='\n'.join(
                                ["A tool to simplify the assignment making process at school level.",
                                 "Write the questions using the conventions as per the documentation,",
                                 "and get the assignment as a formatted .docx file."])
                            )
    parser.add_argument("dir_path",
                        metavar="DIR_PATH",
                        help="full path to the directory (with assets) to process")
    parser.add_argument("txtname",
                        metavar="TEXT_FILE_NAME",
                        help="name of the .txt file (including extension)")
    parser.add_argument("-o", "--docname",
                        metavar="DOCX_FILE_NAME",
                        help="name of the .docx file (including extension; default: assignment.docx)",
                        default="assignment.docx")
    args = parser.parse_args()

    assignment_doc = Assignment(args.dir_path, args.txtname, args.docname)
    assignment_doc.process_title()

    # ask for optional instructions for each question type
    for q_type in assignment_doc.QUESTION_CLS:
        q_type.process_instructions()

    assignment_doc.init_doc()

    if MCQ.QUESTIONS:
        assignment_doc.add_MCQS()
    if AR.QUESTIONS:
        assignment_doc.add_ARS()
    if SUB.QUESTIONS:
        assignment_doc.add_SUBS()
    if not Invalid.QUESTIONS:
        return 
    
    with open(f"{args.dir_path}/invalidated_questions.txt", 'w') as file:
        file.write("THE FOLLOWING QUESTIONS WERE INVALIDATED:\n\n")
        for question in Invalid.QUESTIONS:
            file.writelines(question.statement)
            file.write('\n')


if __name__ == "__main__":
    main()
