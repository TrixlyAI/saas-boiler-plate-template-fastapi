from pydantic import BaseModel
from typing import Optional, Any
from datetime import datetime

class AgentBase(BaseModel):
    name: str
    type: str
    config: Optional[Any] = None
    tenant_id: int

class AgentCreate(AgentBase):
    owner_id: int

class AgentUpdate(BaseModel):
    name: Optional[str] = None
    type: Optional[str] = None
    config: Optional[Any] = None

class AgentOut(AgentBase):
    id: int
    owner_id: int
    created_at: Optional[datetime]
    updated_at: Optional[datetime]

    class Config:
        orm_mode = True 