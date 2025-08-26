from pydantic import BaseModel, field_validator
from uuid import UUID

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