from datetime import datetime
from pydantic import BaseModel


class Rates(BaseModel):
    date_from: datetime
    date_to: datetime
    origin: str
    destination: str
