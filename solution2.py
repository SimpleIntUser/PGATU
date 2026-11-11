import re

with open('students.txt', 'r', encoding='utf-8') as file:
    students = file.read()

with open('scores.txt', 'r', encoding='utf-8') as file:
    scores = file.read()

with open('report.txt', 'w', encoding='utf-8') as file:
    for student, score in zip(students.splitlines(), scores.splitlines()):
        file.write(f"{student}: {score}\n")