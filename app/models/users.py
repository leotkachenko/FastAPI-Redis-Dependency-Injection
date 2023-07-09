from enum import Enum
from datetime import date
from pydantic import BaseModel, UUID4


class Gender(str, Enum):
    MALE = "MALE"
    FEMALE = "FEMALE"


class User(BaseModel):
    __tablename__ = "Users"

    id: UUID4
    first_name: str
    second_name: str
    gender: Gender
    date_of_birth: date
