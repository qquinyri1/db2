from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from faker import Faker
import random
from tables import Student, Group, Teacher, Subject, Grade

engine = create_engine('postgresql://kioka:123321@localhost:5432/postgres')

Session = sessionmaker(bind=engine)
session = Session()

fake = Faker()

groups = []
for _ in range(3):
    group = Group(name=fake.unique.word())
    groups.append(group)
    session.add(group)

teachers = []
for _ in range(random.randint(3, 5)):
    teacher = Teacher(name=fake.name())
    teachers.append(teacher)
    session.add(teacher)

subjects = []
for _ in range(random.randint(5, 8)):
    subject = Subject(name=fake.unique.word(), teacher=random.choice(teachers))
    subjects.append(subject)
    session.add(subject)

students = []
for _ in range(random.randint(30, 50)):
    student = Student(name=fake.name(), group=random.choice(groups))
    students.append(student)
    session.add(student)

for student in students:
    for subject in subjects:
        for _ in range(random.randint(1, 20)):
            grade = Grade(student=student, subject=subject, date=fake.date_between(start_date='-1y', end_date='today'), value=random.randint(1, 5))
            session.add(grade)

with open('seed_data.txt', 'w') as file:
    for _ in range(3):
        group_name = fake.unique.word()
        file.write(f'Group: {group_name}\n')

    for _ in range(random.randint(3, 5)):
        teacher_name = fake.name()
        file.write(f'Teacher: {teacher_name}\n')

    for _ in range(random.randint(5, 8)):
        subject_name = fake.unique.word()
        file.write(f'Subject: {subject_name}\n')

    for _ in range(random.randint(30, 50)):
        student_name = fake.name()
        file.write(f'Student: {student_name}\n')

session.commit()
print(f'groups: {group}')
print(f'teachers: {teachers}')
print(f'subjects: {subjects}')
print(f'students: {students}')