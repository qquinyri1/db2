from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def create_connect():
    engine = create_engine('postgresql://postgres:123321@localhost/kioka')
    Session = sessionmaker(bind=engine)
    session = Session()
    print('connect succesfull')
    return session 


def create_logs(file_name, data):
    with open(file_name, "w") as file:
        for item in data:
            file.write(str(item) + "\n")
    print('logs have been created')



