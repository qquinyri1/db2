from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Student, Group, Teacher, Course, Grade
from connect_and_logs import create_connect , create_logs


fake = Faker()
session = create_connect()

groups = [Group(name=fake.word()) for _ in range(3)]
session.add_all(groups)
session.commit()

teachers = [Teacher(name=fake.name()) for _ in range(3)]
session.add_all(teachers)
session.commit()

courses = [Course(name=fake.word(), teacher=teachers[i % 3]) for i in range(5)]
session.add_all(courses)
session.commit()

students = [Student(name=fake.name(), group=groups[i % 3]) for i in range(50)]
session.add_all(students)
session.commit()

for student in students:
    for course in courses:
        session.add(Grade(student=student, course=course, score=fake.random_int(min=2, max=5)))
session.commit()


def save_to_txt(file_name, data):
    with open(file_name, "w") as file:
        for item in data:
            file.write(str(item) + "\n")

create_logs("groups.txt", [group.name for group in groups])
create_logs("teachers.txt", [teacher.name for teacher in teachers])
create_logs("courses.txt", [course.name for course in courses])
create_logs("students.txt", [student.name for student in students])

