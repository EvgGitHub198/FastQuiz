from app import db
from app import services
from app.models import Question
from sqlalchemy.orm import Session
from fastapi import FastAPI, Depends


app = FastAPI()
db.init_db()


@app.post("/get_random_questions/")
async def get_random_questions(questions_num: int, db: Session = Depends(db.get_db)):
    previous_question = db.query(Question).order_by(Question.id.desc()).first()
    questions = services.fetch_random_question(db, questions_num)
    if previous_question:
        return {
            "id": previous_question.id,
            "question_text": previous_question.question_text,
            "answer_text": previous_question.answer_text,
            "created_at": previous_question.created_at
        }
    else:
        return {}
