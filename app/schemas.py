from pydantic import BaseModel, EmailStr, field_validator, ConfigDict
import re
from datetime import datetime

class RegisterSchema(BaseModel):
    email: EmailStr
    password: str

    @field_validator("password")
    @classmethod
    def validate_password(cls, value):
        if len(value) < 8:
            raise ValueError("Password must be at least 8 characters long")
        if not re.search(r"[A-Z]", value):
            raise ValueError("Password must contain at least one uppercase letter")
        if not re.search(r"[a-z]", value):
            raise ValueError("Password must contain at least one lowercase letter")
        if not re.search(r"[0-9]", value):
            raise ValueError("Password must contain at least one number")
        return value







class LoginSchema(BaseModel):
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime
    model_config = ConfigDict(from_attributes=True)







class FeedbackCreate(BaseModel):
    message: str

class FeedbackResponse(BaseModel):
    id: int
    message: str
    user_id: int

    class Config:
        from_attributes = True    # IMPORTANT for pydantic v2
