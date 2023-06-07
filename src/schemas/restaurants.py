from typing import Optional
from pydantic import BaseModel
from datetime import datetime


class RestaurantsInfo(BaseModel):
    """Базовая схема модели Рестораны"""

    id: int
    name: str
    description: Optional[str]
    address: Optional[str]
    created_at: datetime
    updated_at: datetime
    is_active: bool = True
    user_id: int

    class Config:
        orm_mode = True


class CreateRestaurantsSchema(BaseModel):
    """Базовая схема модели Рестораны"""

    name: str
    description: Optional[str]
    address: Optional[str]
    created_at: datetime
    updated_at: datetime
    is_active: bool
    user_id: int

    class Config:
        orm_mode = True


class UpdateRestaurantsSchema(BaseModel):
    """Cхема для обновления модели Рестораны"""

    name: str
    description: Optional[str]
    address: Optional[str]
    updated_at: datetime
    is_active: bool
    # user_id: int

    class Config:
        orm_mode = True

