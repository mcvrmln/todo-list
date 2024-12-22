from datetime import datetime
from pydantic import BaseModel, field_validator
from typing import Optional


class Item(BaseModel):
    item_id: int
    task: str
    start_date: datetime = datetime.now()
    end_date: datetime | None = None

    @field_validator("end_date", mode="before")
    @classmethod
    def parse_end_date(cls, value):
        if len(value.strip()) == 19:
            return datetime.strptime(value, "%Y-%m-%d %H:%M:%S")
        else:
            return None
