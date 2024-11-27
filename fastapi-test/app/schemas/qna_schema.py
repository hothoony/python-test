from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class QuestionBase(BaseModel):
    title: str
    content: str

class QuestionCreate(QuestionBase):
    pass

class QuestionUpdate(QuestionBase):
    pass

class Question(QuestionBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

class AnswerBase(BaseModel):
    content: str
    question_id: int

class AnswerCreate(AnswerBase):
    pass

class AnswerUpdate(BaseModel):
    content: str

class Answer(AnswerBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None
