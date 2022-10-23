from datetime import datetime
from pydantic import BaseModel, validator


class Rates(BaseModel):
    dateFrom: datetime
    dateTo: datetime
    origin: str
    destination: str

    class Config:
        schema_extra = {
            "example": {
                "dateFrom": "2016-01-15",
                "dateTo": "2016-01-20",
                "origin": "CNGGZ",
                "destination": "FIKTK",
            }
        }

    @validator('dateFrom', 'dateTo', pre=True)
    def check_date_format(cls, values):
        acceptedFormat = "%Y-%m-%d"
        isValidDateFrom = bool(datetime.strptime(values["dateFrom"], acceptedFormat))
        isValidDateTo = bool(datetime.strptime(values["dateTo"], acceptedFormat))
        if not isValidDateFrom or not isValidDateTo:
            raise ValueError('Invalid date format. Date format should be YYYY-MM-DD')
        return values
