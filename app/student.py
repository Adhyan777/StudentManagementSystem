class Student:
    def __init__(self, roll_no, name, age, gender, branch, semester, cgpa, phone, email, address):
        self.roll_no = roll_no
        self.name = name
        self.age = age
        self.gender = gender
        self.branch = branch
        self.semester = semester
        self.cgpa = cgpa
        self.phone = phone
        self.email = email
        self.address = address

    def display(self):
        print("-" * 50)
        print(f"Roll Number : {self.roll_no}")
        print(f"Name        : {self.name}")
        print(f"Age         : {self.age}")
        print(f"Gender      : {self.gender}")
        print(f"Branch      : {self.branch}")
        print(f"Semester    : {self.semester}")
        print(f"CGPA        : {self.cgpa}")
        print(f"Phone       : {self.phone}")
        print(f"Email       : {self.email}")
        print(f"Address     : {self.address}")
        print("-" * 50)

    def to_dict(self):
        return {
            "roll_no": self.roll_no,
            "name": self.name,
            "age": self.age,
            "gender": self.gender,
            "branch": self.branch,
            "semester": self.semester,
            "cgpa": self.cgpa,
            "phone": self.phone,
            "email": self.email,
            "address": self.address
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["roll_no"],
            data["name"],
            data["age"],
            data["gender"],
            data["branch"],
            data["semester"],
            data["cgpa"],
            data["phone"],
            data["email"],
            data["address"]
        )