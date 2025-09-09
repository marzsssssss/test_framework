from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
from typing import List, Optional

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

class TotalAmountModel(BaseModel): 
    currency: CurrencyModel
    amount: str

class CreateEntityEwalletModel(BaseModel):
    created_at: datetime 
    updated_at: datetime
    deleted_at: None
    id: UUID
    number: int
    balance: str
    currency: CurrencyModel
    entity_id: UUID
    type: str

class MetaModel(BaseModel):
    limit: int
    total: int
    current_page: int
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

class GetAccountAmountModel(BaseModel):
    meta: MetaModel
    data: List[Wallet]

class CurrenciesModel(BaseModel):
    created_at: datetime
    updated_at: datetime
    deleted_at: None
    id: UUID
    code: str
    symbol: str
    name: str
    is_popular: bool
    is_used: bool
    priority: int
    file_meta_id: UUID
    flag: str
    is_wallet_exists: bool

class GetEwalletCurrenciesModel(BaseModel):
    data: List[CurrenciesModel]

class GetEwalletsEntityModel(BaseModel):
    created_at: datetime
    updated_at: datetime
    deleted_at: None
    id: UUID
    number: int
    balance: str
    currency: CurrencyModel
    entity_id: UUID
    type: str