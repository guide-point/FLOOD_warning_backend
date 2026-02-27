from typing import Optional, List
from pydantic import BaseModel, Field


class UserCreate(BaseModel):
    device_uuid: str = Field(..., description="Unique device identifier for anonymous registration")
    phone: Optional[str] = Field(None, description="Optional phone number for SMS alerts")
    ward: Optional[str] = Field(None, description="User's ward or city profile")
    language: Optional[str] = Field("en", description="Preferred language code")


class User(BaseModel):
    id: int
    device_uuid: str
    phone: Optional[str]
    ward: Optional[str]
    language: str


class ReportCreate(BaseModel):
    text: str
    photo_url: Optional[str] = Field(None, description="URL to a photo, if any")
    gps: Optional[str] = Field(None, description="GPS coordinates")
    severity: Optional[int] = Field(1, ge=1, le=5)
    ward: Optional[str] = Field(None, description="Ward or city")
    language: Optional[str] = Field(None, description="Language code")


class Report(BaseModel):
    id: int
    text: str
    photo_url: Optional[str]
    gps: Optional[str]
    severity: int
    ward: Optional[str]
    language: Optional[str]
    corroborations: int = 0
    verified: bool = False
