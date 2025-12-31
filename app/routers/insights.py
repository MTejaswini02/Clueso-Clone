from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app import models
from app.auth import get_current_user

router = APIRouter(prefix="/insights", tags=["Insights"])

@router.get("/")
def get_insights(
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):

    user_id = current_user.id    # <-- FINAL FIX

    feedbacks = db.query(models.Feedback).filter(
        models.Feedback.user_id == user_id
    ).all()

    if not feedbacks:
        return {
            "total_feedback": 0,
            "latest_feedback": "No feedback yet",
            "message_length_average": 0
        }

    latest = feedbacks[-1].message
    avg_length = sum(len(f.message) for f in feedbacks) / len(feedbacks)

    return {
        "total_feedback": len(feedbacks),
        "latest_feedback": latest,
        "message_length_average": round(avg_length, 2)
    }
