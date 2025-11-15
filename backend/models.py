from database import Base
from sqlalchemy import Column, Integer, String, JSON, Boolean, ForeignKey
from uuid import uuid4
from datetime import datetime



class User(Base):
    __tablename__ = "users"
    id = Column(String, default=lambda: str(uuid4()), primary_key=True)
    username = Column(String)
    email = Column(String)
    password = Column(String)
    role = Column(String) 



class Question(Base):
    __tablename__ = "questions"

    id = Column(String, default=lambda: str(uuid4()), primary_key=True)
    title = Column(String)
    type = Column(String)
    complexity = Column(String)
    options = Column(JSON, nullable=True)
    correct_answers = Column(JSON, nullable=True)
    max_score = Column(Integer, default=1)



class Exam(Base):
    __tablename__ = "exams"

    id = Column(String, default=lambda: str(uuid4()), primary_key=True)
    title = Column(String)
    start_time = Column(String)
    end_time = Column(String)
    duration = Column(Integer)
    published = Column(Boolean, default=False)

# ok Ok Ok 

 
# Connection of exam and questions tables.
class ExamQuestionBank (Base):
    __tablename__ = "exam_questions"

    id = Column(String, default=lambda: str(uuid4()), primary_key=True)
    exam_id = Column(String, ForeignKey("exams.id"))
    question_id = Column(String, ForeignKey("questions.id")) 




    