# ezAssignments

A project to simplify assignment-making tasks at school level.

If you wish to add new questions for your own usage purposes, follow the convention used to write the original `assignment.txt`

### Convention to write `.txt` files for assignments
`<QUESTION_CODE>: MCQ, AR, SUB`

Questions are separated by two newline characters.

Follow the given snippet to write your assignments.

```commandline
MCQ
Question 
spanning over
multiple lines

Option A..
Option B..
Option C..
Option D..


AR
Assertion spanning 
over multiple lines

Notice the newline between the assertion
and the reason statement


SUB
A subjective question
that spans over multiple lines.
Pretty simple to write these,
Right?


P.S.
This question is invalid,
since it has no valid question tag before it.
```

Although here the question statement spans over multiple lines, it won't be the case with the actual assignment document.

Invalidated questions are saved in `invalidated_questions.txt`

```commandline
THE FOLLOWING QUESTIONS WERE INVALIDATED:

P.S.
This question is invalid,
since it has no valid question tag before it.


```


### How to Run

1. Navigate to the project directory:
`~/ezAssignments/ezassignments`
2. Run: `python main.py`
```commandline
usage: main.py [-h] [-o DOCX_FILE_NAME] dir_path TEXT_FILE_NAME

A tool to simplify the assignment making process at school level. 
Write the questions using the conventions as per the documentation, 
and get the assignment as a formatted .docx file.

positional arguments:
  dir_path              full path to the directory (with assets) to process
  TEXT_FILE_NAME        name of the .txt file

options:
  -h, --help            show this help message and exit
  -o DOCX_FILE_NAME, --docxname DOCX_FILE_NAME
                        name of the .docx file (default: assignment)
```

3. Follow the usage instructions to use the program.