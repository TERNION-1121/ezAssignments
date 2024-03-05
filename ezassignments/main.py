from argparse import ArgumentParser
from src import Assignment


def main():
    # arg name should also be the filename of the .txt file
    parser = ArgumentParser(prog="main.py",
                            description='\n'.join(
                                ["A tool to simplify the assignment making process at school level.",
                                 "Write the questions using the conventions as per the documentation,",
                                 "and get the assignment as a formatted .docx file."])
                            )
    parser.add_argument("dir_path",
                        help="full path to the directory (with assets) to process")
    parser.add_argument("txt_file_name",
                        metavar="TEXT_FILE_NAME",
                        help="name of the .txt file")
    parser.add_argument("-o", "--docxname",
                        metavar="DOCX_FILE_NAME",
                        help="name of the .docx file (default: assignment)",
                        default="assignment")
    args = parser.parse_args()

    assignment = Assignment(args.dir_path, args.txt_file_name, args.docxname)
    assignment.init_doc()

    if assignment.QUESTIONS["MCQS"]:
        assignment.add_MCQS()
    if assignment.QUESTIONS["ARS"]:
        assignment.add_ARS()
    if assignment.QUESTIONS["SUBS"]:
        assignment.add_SUBS()
    if not assignment.QUESTIONS["INVALIDATED"]:
        return 
    
    with open(f"{args.dir_path}/invalidated_questions.txt", 'w') as file:
        file.write("THE FOLLOWING QUESTIONS WERE INVALIDATED:\n\n")
        for question in assignment.QUESTIONS["INVALIDATED"]:
            for line in question:
                file.write(line + '\n')
            file.write('\n')


if __name__ == "__main__":
    main()
