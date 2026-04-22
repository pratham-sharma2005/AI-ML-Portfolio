from langchain_text_splitters import RecursiveCharacterTextSplitter,Language

text ="""
import random

class Student:
    def __init__(self, name):
        self.name = name
        self.marks = []

    def add_marks(self, mark):
        self.marks.append(mark)

    def average(self):
        if len(self.marks) == 0:
            return 0
        return sum(self.marks) / len(self.marks)

    def display(self):
        print("Student:", self.name)
        print("Marks:", self.marks)
        print("Average:", round(self.average(), 2))
        print("-" * 30)


# Create students
students = [
    Student("Alice"),
    Student("Bob"),
    Student("Charlie")
]

# Add random marks
for student in students:
    for i in range(5):
        mark = random.randint(50, 100)
        student.add_marks(mark)

# Display data
for student in students:
    student.display()

# Find top performer
top_student = None
highest_avg = 0

for student in students:
    avg = student.average()
    if avg > highest_avg:
        highest_avg = avg
        top_student = student

print("Top Performer:", top_student.name, "with average", round(highest_avg, 2))
"""

splitter = RecursiveCharacterTextSplitter.from_language(
    language = Language.PYTHON,
    chunk_size = 100,
    chunk_overlap = 0
)

chunks = splitter.split_text(text)

print(len(chunks))

print(chunks[1])