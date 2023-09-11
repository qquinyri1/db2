from sqlalchemy import func, desc
from tables import Student, Grade, Group, Teacher, Subject, engine
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

def select_1():
    query = session.query(Student.name, func.round(func.avg(Grade.value), 2).label('avg_grade')) \
        .join(Grade).group_by(Student.id).order_by(desc('avg_grade')).limit(5)
    return query.all()

def select_2(subject_name):
    query = session.query(Student.name, func.round(func.avg(Grade.value), 2).label('avg_grade')) \
        .join(Grade).join(Subject).filter(Subject.name == subject_name).group_by(Student.id).order_by(desc('avg_grade')).limit(1)
    return query.first()

def select_3(subject_name):
    query = session.query(Group.name, func.round(func.avg(Grade.value), 2).label('avg_grade')) \
        .select_from(Group) \
        .join(Student).join(Grade).join(Subject).filter(Subject.name == subject_name) \
        .group_by(Group.name)
    return query.all()

def select_4():
    query = session.query(func.round(func.avg(Grade.value), 2).label('avg_grade'))
    return query.scalar()

def select_5(teacher_name):
    query = session.query(Subject.name).join(Teacher).filter(Teacher.name == teacher_name)
    return query.all()

def select_6(group_name):
    query = session.query(Student.name).join(Group).filter(Group.name == group_name)
    return query.all()

def select_7(group_name, subject_name):
    query = session.query(Student.name, Grade.value) \
        .join(Group).join(Grade).join(Subject).filter(Group.name == group_name, Subject.name == subject_name)
    return query.all()

def select_8(teacher_name):
    query = session.query(func.round(func.avg(Grade.value), 2).label('avg_grade')) \
        .join(Subject).join(Teacher).filter(Teacher.name == teacher_name)
    return query.scalar()


def select_9(student_name):
    query = session.query(Subject.name) \
        .join(Grade) \
        .join(Student) \
        .filter(Student.name == student_name)
    return query.all()

def select_10(student_name, teacher_name):
    query = session.query(Subject.name) \
        .join(Grade, Grade.subject_id == Subject.id) \
        .join(Student, Student.id == Grade.student_id) \
        .join(Teacher, Teacher.id == Subject.teacher_id) \
        .filter(Student.name == student_name, Teacher.name == teacher_name)
    return query.all()


print(select_1())
print(select_2(subject_name='old'))
print(select_3(subject_name='old'))
print(select_4())
print(select_5('Luis Burns'))
print(select_6('information'))
print(select_7(group_name='information', subject_name='old'))
print(select_8('Luis Burns'))
print(select_9('David Potter'))
print(select_10(student_name='David Potter', teacher_name='Luis Burns'))