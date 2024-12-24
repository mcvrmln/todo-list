from datetime import date, datetime
from tkinter import NO
from pydantic import BaseModel, field_validator
from typing import Optional
from dateutil.parser import isoparse


class Item(BaseModel):
    item_id: int | None = None
    task: str
    start_date: datetime = datetime.now()
    end_date: datetime | None = None

    def done(self):
        self.end_date = datetime.now()
