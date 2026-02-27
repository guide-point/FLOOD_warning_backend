from fastapi import APIRouter, Depends, HTTPException
from typing import List, Optional
from pydantic import BaseModel

from sqlalchemy.orm import Session

from models.db import get_db
from models import orm

router = APIRouter()


class SOSEvent(BaseModel):
    id: int
    user_id: Optional[int]
    gps: Optional[str]
    timestamp: Optional[str]
    active: bool = True


@router.post("/", response_model=SOSEvent)
def create_sos(user_id: Optional[int] = None, gps: Optional[str] = None, db: Session = Depends(get_db)):
    event = orm.SOSEvent(
        user_id=user_id,
        gps=gps,
    )
    db.add(event)
    db.commit()
    db.refresh(event)
    # dispatch logic would go here
    return event


@router.get("/active", response_model=List[SOSEvent])
def get_active(city: Optional[str] = None, db: Session = Depends(get_db)):
    query = db.query(orm.SOSEvent).filter(orm.SOSEvent.active == True)
    # city filtering stubbed
    return query.all()


@router.delete("/{sos_id}")
def cancel_sos(sos_id: int, db: Session = Depends(get_db)):
    event = db.query(orm.SOSEvent).get(sos_id)
    if not event:
        raise HTTPException(status_code=404, detail="SOS event not found")
    event.active = False
    db.commit()
    return {"status": "canceled"}
