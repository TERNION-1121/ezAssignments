from os import getcwd
from platform import system

from src.assignment import Assignment

file_path = getcwd() + ('\\' if system() == 'windows' else '/') + "assignment.txt"
assignment = Assignment(file_path)
