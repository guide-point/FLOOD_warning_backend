from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from models.schemas import UserCreate, User
from models import orm
from models.db import get_db

router = APIRouter()


@router.post("/register", response_model=User)
def register_user(payload: UserCreate, db: Session = Depends(get_db)):
    # look for existing device
    existing = db.query(orm.User).filter(orm.User.device_uuid == payload.device_uuid).first()
    if existing:
        return existing

    user_obj = orm.User(
        device_uuid=payload.device_uuid,
        phone=payload.phone,
        ward=payload.ward,
        language=payload.language or "en",
    )
    db.add(user_obj)
    db.commit()
    db.refresh(user_obj)
    return user_obj


@router.get("/{user_id}", response_model=User)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user_obj = db.query(orm.User).get(user_id)
    if not user_obj:
        raise HTTPException(status_code=404, detail="User not found")
    return user_obj
