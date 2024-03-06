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
                        help="name of the .txt file")
    parser.add_argument("-o", "--docname",
                        metavar="DOCX_FILE_NAME",
                        help="name of the .docx file (default: assignment)",
                        default="assignment")
    args = parser.parse_args()

    assignment_doc = Assignment(args.dir_path, args.txt_file_name, args.docxname)
    # ask for optional instructions for each question type
    for question_type in assignment_doc.QUESTIONS.keys():
        if question_type == "INVALIDATED":
            break
        question_type.process_instructions()

    assignment_doc.init_doc()

    if assignment_doc.QUESTIONS[MCQ]:
        assignment_doc.add_MCQS()
    if assignment_doc.QUESTIONS[AR]:
        assignment_doc.add_ARS()
    if assignment_doc.QUESTIONS[SUB]:
        assignment_doc.add_SUBS()
    if not assignment_doc.QUESTIONS["INVALIDATED"]:
        return 
    
    with open(f"{args.dir_path}/invalidated_questions.txt", 'w') as file:
        file.write("THE FOLLOWING QUESTIONS WERE INVALIDATED:\n\n")
        for question in assignment_doc.QUESTIONS["INVALIDATED"]:
            for line in question:
                file.write(line + '\n')
            file.write('\n')


if __name__ == "__main__":
    main()
