import json
import os

from app.student import Student


FILE_PATH = "data/students.json"


def load_students():
    if not os.path.exists(FILE_PATH):
        return []

    try:
        with open(FILE_PATH, "r") as file:
            data = json.load(file)
            return [Student.from_dict(student) for student in data]
    except (json.JSONDecodeError, FileNotFoundError):
        return []


def save_students(students):
    with open(FILE_PATH, "w") as file:
        json.dump(
            [student.to_dict() for student in students],
            file,
            indent=4
        )