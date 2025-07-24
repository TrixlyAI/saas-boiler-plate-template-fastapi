from pydantic import BaseModel
from typing import Optional, Any
from datetime import datetime

class JobBase(BaseModel):
    crew_id: Optional[int] = None
    agent_id: Optional[int] = None
    input_data: Optional[Any] = None
    output_data: Optional[Any] = None
    status: str = "pending"

class JobCreate(JobBase):
    pass

class JobUpdate(BaseModel):
    status: Optional[str] = None
    output_data: Optional[Any] = None
    finished_at: Optional[datetime] = None

class JobOut(JobBase):
    id: int
    started_at: Optional[datetime]
    finished_at: Optional[datetime]

    class Config:
        orm_mode = True 