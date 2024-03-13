# ezAssignments

A project to simplify assignment-making tasks at school level.

### Convention to write `.txt` files for assignments
`<QUESTION_CODE>: MCQ, AR, SUB`

Questions are separated by two newline characters.

In order to add images, create an `images` subdirectory in the provided directory path
and have your image assets there. Then, if you wish to add an image before any question, 
use the following syntax after the whole question text (in a newline) to add one, `[image_name.extension]`

Remember if you don't wish to add an image, just proceed as usual without using that line of text.

Follow the given snippet to write your assignments.

```commandline
MCQ
Question 
spanning over
multiple lines
[image_name.extension]

Option A..
Option B..
Option C..
Option D..


AR
Assertion spanning 
over multiple lines

Notice the newline between the assertion
and the reason statement
[image_name.extension]


SUB
A subjective question
that spans over multiple lines.
Pretty simple to write these,
Right?
[image_name.extension]


P.S.
This question is invalid,
since it has no valid question tag before it.
```

Although here the question statement spans over multiple lines, it won't be the case with the actual assignment document.

Information about invalidated questions and images is saved in `invalidated.txt`

```commandline
THE FOLLOWING QUESTIONS WERE INVALIDATED:

P.S.
This question is invalid,
since it has no valid question tag before it.


```

<br>

![image](https://github.com/TERNION-1121/ezAssignments/assets/97667653/1ce59e3c-e5f5-4964-bff3-3be6bdeacf2f)

> Result document

### How to Run

1. Navigate to the project directory:
`~/ezAssignments/ezassignments`
2. Run: `python main.py`
```commandline
usage: main.py [-h] [-o DOCX_FILE_NAME] DIR_PATH TEXT_FILE_NAME

A tool to simplify the assignment making process at school level. 
Write the questions using the conventions as per the documentation, 
and get the assignment as a formatted .docx file.     

positional arguments:
  DIR_PATH              full path to the directory (with assets) to process
  TEXT_FILE_NAME        name of the .txt file (including extension)

options:
  -h, --help            show this help message and exit
  -o DOCX_FILE_NAME, --docname DOCX_FILE_NAME
                        name of the .docx file (including extension; default: assignment.docx)
```

3. Follow the usage instructions to use the program.
