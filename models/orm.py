from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.orm import relationship
import datetime

from .db import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    device_uuid = Column(String, unique=True, index=True, nullable=False)
    phone = Column(String, nullable=True)
    ward = Column(String, nullable=True)
    language = Column(String, default="en")


class Report(Base):
    __tablename__ = "reports"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(String, nullable=False)
    photo_url = Column(String, nullable=True)
    gps = Column(String, nullable=True)
    severity = Column(Integer, default=1)
    ward = Column(String, nullable=True)
    language = Column(String, nullable=True)
    corroborations = Column(Integer, default=0)
    verified = Column(Boolean, default=False)


class SOSEvent(Base):
    __tablename__ = "sos_events"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, nullable=True)
    gps = Column(String, nullable=True)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)
    active = Column(Boolean, default=True)
