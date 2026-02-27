from fastapi import APIRouter, Depends, HTTPException
from typing import List, Optional
from sqlalchemy.orm import Session

from models.schemas import ReportCreate, Report
from models import orm
from models.db import get_db

router = APIRouter()


@router.post("/", response_model=Report)
def create_report(payload: ReportCreate, db: Session = Depends(get_db)):
    report_obj = orm.Report(
        text=payload.text,
        photo_url=payload.photo_url,
        gps=payload.gps,
        severity=payload.severity,
        ward=payload.ward,
        language=payload.language,
    )
    db.add(report_obj)
    db.commit()
    db.refresh(report_obj)
    return report_obj


@router.get("/", response_model=List[Report])
def list_reports(
    ward: Optional[str] = None,
    severity: Optional[int] = None,
    verified: Optional[bool] = None,
    db: Session = Depends(get_db),
):
    query = db.query(orm.Report)
    if ward:
        query = query.filter(orm.Report.ward == ward)
    if severity is not None:
        query = query.filter(orm.Report.severity == severity)
    if verified is not None:
        query = query.filter(orm.Report.verified == verified)
    return query.all()


@router.post("/{report_id}/confirm", response_model=Report)
def confirm_report(report_id: int, db: Session = Depends(get_db)):
    report_obj = db.query(orm.Report).get(report_id)
    if not report_obj:
        raise HTTPException(status_code=404, detail="Report not found")
    report_obj.corroborations += 1
    if report_obj.corroborations >= 3:
        report_obj.verified = True
    db.commit()
    db.refresh(report_obj)
    return report_obj
