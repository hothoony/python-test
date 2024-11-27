from typing import Dict, List, Optional
import logging
from app.models.qna_model import QnAModel
from app.schemas.qna_schema import QuestionCreate, QuestionUpdate, AnswerCreate, AnswerUpdate

logger = logging.getLogger(__name__)

class QnAService:
    def __init__(self):
        self.model = QnAModel()

    # Question 관련 서비스
    def create_question(self, question: QuestionCreate) -> Dict:
        logger.debug(f"Creating new question: {question.model_dump()}")
        result = self.model.create_question(question)
        logger.info(f"Successfully created question with id: {result['id']}")
        return result

    def get_questions(self) -> List[Dict]:
        logger.debug("Retrieving all questions")
        return self.model.get_questions()

    def get_question(self, question_id: int) -> Optional[Dict]:
        logger.debug(f"Retrieving question with id: {question_id}")
        question = self.model.get_question(question_id)
        if question is None:
            logger.warning(f"Question not found with id: {question_id}")
        return question

    def update_question(self, question_id: int, question: QuestionUpdate) -> Optional[Dict]:
        logger.debug(f"Updating question {question_id} with data: {question.model_dump()}")
        result = self.model.update_question(question_id, question)
        if result is None:
            logger.error(f"Failed to update question with id: {question_id}")
        else:
            logger.info(f"Successfully updated question {question_id}")
        return result

    def delete_question(self, question_id: int) -> Optional[Dict]:
        logger.debug(f"Deleting question with id: {question_id}")
        result = self.model.delete_question(question_id)
        if result is None:
            logger.error(f"Failed to delete question with id: {question_id}")
        else:
            logger.info(f"Successfully deleted question {question_id}")
        return result

    # Answer 관련 서비스
    def create_answer(self, answer: AnswerCreate) -> Optional[Dict]:
        logger.debug(f"Creating new answer for question {answer.question_id}: {answer.model_dump()}")
        result = self.model.create_answer(answer)
        if result is None:
            logger.error(f"Failed to create answer: question {answer.question_id} not found")
        else:
            logger.info(f"Successfully created answer with id: {result['id']}")
        return result

    def get_answers(self, question_id: int) -> List[Dict]:
        logger.debug(f"Retrieving all answers for question: {question_id}")
        return self.model.get_answers(question_id)

    def get_answer(self, answer_id: int) -> Optional[Dict]:
        logger.debug(f"Retrieving answer with id: {answer_id}")
        answer = self.model.get_answer(answer_id)
        if answer is None:
            logger.warning(f"Answer not found with id: {answer_id}")
        return answer

    def update_answer(self, answer_id: int, answer: AnswerUpdate) -> Optional[Dict]:
        logger.debug(f"Updating answer {answer_id} with data: {answer.model_dump()}")
        result = self.model.update_answer(answer_id, answer)
        if result is None:
            logger.error(f"Failed to update answer with id: {answer_id}")
        else:
            logger.info(f"Successfully updated answer {answer_id}")
        return result

    def delete_answer(self, answer_id: int) -> Optional[Dict]:
        logger.debug(f"Deleting answer with id: {answer_id}")
        result = self.model.delete_answer(answer_id)
        if result is None:
            logger.error(f"Failed to delete answer with id: {answer_id}")
        else:
            logger.info(f"Successfully deleted answer {answer_id}")
        return result
