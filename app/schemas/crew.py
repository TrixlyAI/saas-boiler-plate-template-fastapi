from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class CrewBase(BaseModel):
    name: str
    description: Optional[str] = None
    tenant_id: int

class CrewCreate(CrewBase):
    owner_id: int

class CrewUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None

class CrewOut(CrewBase):
    id: int
    owner_id: int
    created_at: Optional[datetime]
    updated_at: Optional[datetime]

    class Config:
        orm_mode = True 