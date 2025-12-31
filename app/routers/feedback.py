
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app import models
from app.schemas import FeedbackCreate, FeedbackResponse
from app.auth import get_current_user

router = APIRouter(prefix="/feedback", tags=["Feedback"])

@router.post("/", response_model=FeedbackResponse)
def create_feedback(
    feedback: FeedbackCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    new_feedback = models.Feedback(
        message=feedback.message,
        user_id=current_user.id
    )

    db.add(new_feedback)
    db.commit()
    db.refresh(new_feedback)   # <-- THIS generates real ID

    return new_feedback


@router.get("/", response_model=list[FeedbackResponse])
def get_feedbacks(
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    feedbacks = (
        db.query(models.Feedback)
        .filter(models.Feedback.user_id == current_user.id)
        .all()
    )
    return feedbacks
