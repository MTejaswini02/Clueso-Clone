from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app import auth
from app.database import get_db
from app.models import User
from app.schemas import RegisterSchema, LoginSchema

router = APIRouter(prefix="/auth", tags=["Auth"])


# ---------- REGISTER ----------
@router.post("/register")
def register(user: RegisterSchema, db: Session = Depends(get_db)):

    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="User already exists")

    hashed = auth.hash_password(user.password)

    new_user = User(
        email=user.email,
        password=hashed
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {"message": "User registered successfully"}


# ---------- LOGIN ----------
@router.post("/login")
def login(user: LoginSchema, db: Session = Depends(get_db)):

    db_user = db.query(User).filter(User.email == user.email).first()
    if not db_user:
        raise HTTPException(status_code=400, detail="Invalid credentials")

    if not auth.verify_password(user.password, db_user.password):
        raise HTTPException(status_code=400, detail="Invalid credentials")

    token = auth.create_access_token({"sub": db_user.email, "id": db_user.id})

    return {
        "message": "Login successful",
        "token": token
    }
