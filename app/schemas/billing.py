from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class BillingBase(BaseModel):
    user_id: int
    customer_id: str
    subscription_id: Optional[str] = None
    plan: str
    active: bool = True

class BillingCreate(BillingBase):
    pass

class BillingOut(BillingBase):
    id: int
    created_at: Optional[datetime]
    updated_at: Optional[datetime]

    class Config:
        orm_mode = True 