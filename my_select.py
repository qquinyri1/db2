from sqlalchemy import  func,desc 
from models import Student, Group, Teacher, Course, Grade
from connect_and_logs import create_connect


session = create_connect()

def select_1():
    result = session.query(Student.name, func.avg(Grade.score).label('avg_grade'))\
        .join(Grade, Student.id == Grade.student_id)\
        .group_by(Student.name)\
        .order_by(desc('avg_grade'))\
        .limit(5).all()
    return result

def select_2(course_name):
    result = session.query(Student.name, func.avg(Grade.score).label('avg_grade'))\
        .join(Grade, Student.id == Grade.student_id)\
        .join(Course, Course.id == Grade.course_id)\
        .filter(Course.name == course_name)\
        .group_by(Student.name)\
        .order_by(desc('avg_grade'))\
        .first()
    return result

def select_3(course_name):
    result = session.query(Group.name, func.avg(Grade.score).label('avg_grade'))\
        .join(Student, Group.id == Student.group_id)\
        .join(Grade, Student.id == Grade.student_id)\
        .join(Course, Course.id == Grade.course_id)\
        .filter(Course.name == course_name)\
        .group_by(Group.name)\
        .all()
    return result

def select_4():
    result = session.query(func.avg(Grade.score).label('avg_grade')).scalar()
    return result

def select_5(teacher_name):
    result = session.query(Course.name)\
        .join(Teacher, Teacher.id == Course.teacher_id)\
        .filter(Teacher.name == teacher_name)\
        .all()
    return result

def select_6(group_name):
    result = session.query(Student.name)\
        .join(Group, Student.group_id == Group.id)\
        .filter(Group.name == group_name)\
        .all()
    return result

def select_7(group_name, course_name):
    result = session.query(Student.name, Grade.score)\
        .join(Group, Student.group_id == Group.id)\
        .join(Grade, Student.id == Grade.student_id)\
        .join(Course, Course.id == Grade.course_id)\
        .filter(Group.name == group_name, Course.name == course_name)\
        .all()
    return result

def select_8(teacher_name):
    result = session.query(func.avg(Grade.score).label('avg_grade'))\
        .join(Course, Course.id == Grade.course_id)\
        .join(Teacher, Teacher.id == Course.teacher_id)\
        .filter(Teacher.name == teacher_name)\
        .scalar()
    return result

def select_9(student_name):
    result = session.query(Course.name)\
        .join(Grade, Course.id == Grade.course_id)\
        .join(Student, Student.id == Grade.student_id)\
        .filter(Student.name == student_name)\
        .distinct()\
        .all()
    return result

def select_10(student_name, teacher_name):
    result = session.query(Course.name)\
        .join(Grade, Course.id == Grade.course_id)\
        .join(Student, Student.id == Grade.student_id)\
        .join(Teacher, Teacher.id == Course.teacher_id)\
        .filter(Student.name == student_name, Teacher.name == teacher_name)\
        .distinct()\
        .all()
    return result

if __name__ == "__main__":
    print("Запрос 1:")
    result_1 = select_1()
    print(result_1)

    print("\nЗапрос 2:")
    result_2 = select_2("economy")
    print(result_2)

    print("\nЗапрос 3:")
    result_3 = select_3("economy")
    print(result_3)

    print("\nЗапрос 4:")
    result_4 = select_4()
    print(result_4)

    print("\nЗапрос 5:")
    result_5 = select_5("Beth Garcia")
    print(result_5)

    print("\nЗапрос 6:")
    result_6 = select_6("relate")
    print(result_6)

    print("\nЗапрос 7:")
    result_7 = select_7("relate", "economy")
    print(result_7)

    print("\nЗапрос 8:")
    result_8 = select_8("Beth Garcia")
    print(result_8)

    print("\nЗапрос 9:")
    result_9 = select_9("Kathleen Wilcox")  
    print(result_9)

    print("\nЗапрос 10:")
    result_10 = select_10("Kathleen Wilcox", "Beth Garcia")  
    print(result_10)


