from fastapi import APIRouter, HTTPException, status
from typing import List
from app.schemas.qna_schema import (
    QuestionCreate, QuestionUpdate, Question,
    AnswerCreate, AnswerUpdate, Answer
)
from app.services.qna_service import QnAService

router = APIRouter(prefix="/qna", tags=["QnA"])
service = QnAService()

# Question endpoints
@router.post("/questions", response_model=Question, status_code=status.HTTP_201_CREATED)
def create_question(question: QuestionCreate):
    return service.create_question(question)

@router.get("/questions", response_model=List[Question])
def get_questions():
    return service.get_questions()

@router.get("/questions/{question_id}", response_model=Question)
def get_question(question_id: int):
    question = service.get_question(question_id)
    if question is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Question with id {question_id} not found"
        )
    return question

@router.put("/questions/{question_id}", response_model=Question)
def update_question(question_id: int, question: QuestionUpdate):
    updated_question = service.update_question(question_id, question)
    if updated_question is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Question with id {question_id} not found"
        )
    return updated_question

@router.delete("/questions/{question_id}", response_model=Question)
def delete_question(question_id: int):
    deleted_question = service.delete_question(question_id)
    if deleted_question is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Question with id {question_id} not found"
        )
    return deleted_question

# Answer endpoints
@router.post("/questions/{question_id}/answers", response_model=Answer, status_code=status.HTTP_201_CREATED)
def create_answer(question_id: int, answer: AnswerCreate):
    if answer.question_id != question_id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Question ID in path and body must match"
        )
    created_answer = service.create_answer(answer)
    if created_answer is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Question with id {question_id} not found"
        )
    return created_answer

@router.get("/questions/{question_id}/answers", response_model=List[Answer])
def get_answers(question_id: int):
    return service.get_answers(question_id)

@router.get("/answers/{answer_id}", response_model=Answer)
def get_answer(answer_id: int):
    answer = service.get_answer(answer_id)
    if answer is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Answer with id {answer_id} not found"
        )
    return answer

@router.put("/answers/{answer_id}", response_model=Answer)
def update_answer(answer_id: int, answer: AnswerUpdate):
    updated_answer = service.update_answer(answer_id, answer)
    if updated_answer is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Answer with id {answer_id} not found"
        )
    return updated_answer

@router.delete("/answers/{answer_id}", response_model=Answer)
def delete_answer(answer_id: int):
    deleted_answer = service.delete_answer(answer_id)
    if deleted_answer is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Answer with id {answer_id} not found"
        )
    return deleted_answer
