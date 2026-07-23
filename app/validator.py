import re


def validate_roll_no(roll_no):
    return roll_no.strip() != ""


def validate_name(name):
    return name.replace(" ", "").isalpha()


def validate_age(age):
    try:
        age = int(age)
        return 16 <= age <= 100
    except ValueError:
        return False


def validate_gender(gender):
    gender = gender.lower()
    return gender in ["male", "female", "other"]


def validate_branch(branch):
    return branch.strip() != ""


def validate_semester(semester):
    try:
        semester = int(semester)
        return 1 <= semester <= 8
    except ValueError:
        return False


def validate_cgpa(cgpa):
    try:
        cgpa = float(cgpa)
        return 0 <= cgpa <= 10
    except ValueError:
        return False


def validate_phone(phone):
    return phone.isdigit() and len(phone) == 10


def validate_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None


def validate_address(address):
    return address.strip() != ""