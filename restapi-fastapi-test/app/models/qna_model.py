from typing import Dict, List, Optional
from datetime import datetime
from app.schemas.qna_schema import QuestionCreate, QuestionUpdate, AnswerCreate, AnswerUpdate

class QnAModel:
    def __init__(self):
        self.questions: List[Dict] = []
        self.answers: List[Dict] = []
        self.question_id_counter = 0
        self.answer_id_counter = 0

    def create_question(self, question: QuestionCreate) -> Dict:
        question_dict = question.model_dump()
        question_dict.update({
            "id": self.question_id_counter,
            "created_at": datetime.now(),
            "updated_at": None
        })
        self.questions.append(question_dict)
        self.question_id_counter += 1
        return question_dict

    def get_questions(self) -> List[Dict]:
        return self.questions

    def get_question(self, question_id: int) -> Optional[Dict]:
        for question in self.questions:
            if question["id"] == question_id:
                return question
        return None

    def update_question(self, question_id: int, question: QuestionUpdate) -> Optional[Dict]:
        for idx, q in enumerate(self.questions):
            if q["id"] == question_id:
                question_dict = question.model_dump()
                question_dict.update({
                    "id": question_id,
                    "created_at": q["created_at"],
                    "updated_at": datetime.now()
                })
                self.questions[idx] = question_dict
                return question_dict
        return None

    def delete_question(self, question_id: int) -> Optional[Dict]:
        for idx, question in enumerate(self.questions):
            if question["id"] == question_id:
                # 관련된 답변들도 삭제
                self.answers = [a for a in self.answers if a["question_id"] != question_id]
                return self.questions.pop(idx)
        return None

    def create_answer(self, answer: AnswerCreate) -> Optional[Dict]:
        # 질문이 존재하는지 확인
        if not any(q["id"] == answer.question_id for q in self.questions):
            return None
        
        answer_dict = answer.model_dump()
        answer_dict.update({
            "id": self.answer_id_counter,
            "created_at": datetime.now(),
            "updated_at": None
        })
        self.answers.append(answer_dict)
        self.answer_id_counter += 1
        return answer_dict

    def get_answers(self, question_id: int) -> List[Dict]:
        return [a for a in self.answers if a["question_id"] == question_id]

    def get_answer(self, answer_id: int) -> Optional[Dict]:
        for answer in self.answers:
            if answer["id"] == answer_id:
                return answer
        return None

    def update_answer(self, answer_id: int, answer: AnswerUpdate) -> Optional[Dict]:
        for idx, a in enumerate(self.answers):
            if a["id"] == answer_id:
                answer_dict = a.copy()
                answer_dict.update({
                    "content": answer.content,
                    "updated_at": datetime.now()
                })
                self.answers[idx] = answer_dict
                return answer_dict
        return None

    def delete_answer(self, answer_id: int) -> Optional[Dict]:
        for idx, answer in enumerate(self.answers):
            if answer["id"] == answer_id:
                return self.answers.pop(idx)
        return None
