import mysql.connector
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = sqlalchemy.create_engine('mysql+mysqlconnector://root:abc123@localhost:3306/dbtestowa',echo=True)

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = sqlalchemy.Column(sqlalchemy.Integer,primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.String(length=50))
    fullname = sqlalchemy.Column(sqlalchemy.String(length=50))
    nickname = sqlalchemy.Column(sqlalchemy.String(length=50))

    def __repr__(self):
        return f'<User(name={self.name}, fullname={self.fullname}, nickname={self.nickname})>'

Base.metadata.create_all(engine)

Session = sqlalchemy.orm.sessionmaker()
Session.configure(bind=engine)
session = Session()

#dodaj usera

pr_user = User(name='Marcin', fullname='Marcin Albiniak', nickname='albim')
session.add(pr_user)

dr_user = User(name='Kleopatra', fullname='Kleopatra Bryk', nickname='Cleo')
session.add(dr_user)

session.commit()
print("____________Wszyscy użytkownicy_________________")
for s in session.query(User).all():
    print(s.fullname,s.nickname)
print("__________użytkownik o nickname -> albim____________")
for s in session.query(User).filter(User.nickname=="albim"):
    print(s.fullname,s.nickname)
