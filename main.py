from os import getcwd
from platform import system

from src.assignment_maker import Assignment

file_path = getcwd() + ('\\' if system() == 'windows' else '/') + "assignment.txt"
assignment = Assignment(file_path)

print(assignment)