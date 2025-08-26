from pydantic import BaseModel, field_validator
from uuid import UUID
from datetime import datetime

class CurrencyModel(BaseModel):
    id: UUID
    code: str
    symbol: str
    name: str
    is_popular: bool
    is_used: bool
    priority: int
    file_meta_id: UUID
    flag: str | None

class AccountsModel(BaseModel): 
    currency: CurrencyModel
    amount: str

class CreateEntityEwallet(BaseModel):
    created_at: datetime 
    updated_at: datetime
    deleted_at: None
    id: UUID
    number: int
    balance: str
    currency: CurrencyModel
    entity_id: UUID
    type: str