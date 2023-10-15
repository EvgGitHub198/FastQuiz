import requests
from app.models import Question
from app.config import QUIZ_API_URL
from fastapi import HTTPException
from sqlalchemy.orm import Session


def fetch_random_question(db: Session, questions_num: int):
    questions = []

    for _ in range(questions_num):
        response = requests.get(QUIZ_API_URL)
        if response.status_code == 200:
            question_data = response.json()[0]
            existing_question = db.query(Question).filter_by(question_text=question_data['question']).first()

            while existing_question:
                response = requests.get(QUIZ_API_URL)
                question_data = response.json()[0]
                existing_question = db.query(Question).filter_by(question_text=question_data['question']).first()

            created_at = question_data['created_at']

            question = Question(
                question_text=question_data['question'],
                answer_text=question_data['answer'],
                created_at=created_at

            )
            db.add(question)
            db.commit()
            db.refresh(question)
            questions.append(question)
        else:
            raise HTTPException(status_code=500, detail="Не удалось получить вопросы из внешнего API")

    return questions
