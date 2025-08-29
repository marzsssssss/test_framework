from pydantic import BaseModel
from uuid import UUID
from typing import List
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

class MetaModel(BaseModel):
    limit: int
    total: int
    currency_page: int
    last_page: int

class Wallet(BaseModel):
    created_at: datetime
    updated_at: datetime
    deleted_at: None
    id: UUID
    number: int
    balance: str
    currency: CurrencyModel
    entity_id: UUID
    type: str

class GetEntitiesModel(BaseModel):
    meta: MetaModel
    data: List[Wallet]
