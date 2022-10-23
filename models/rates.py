from datetime import datetime
from pydantic import BaseModel, validator


class Rates(BaseModel):
    dateFrom: datetime
    dateTo: datetime
    origin: str
    destination: str

    @validator('dateFrom', 'dateTo', pre=True)
    def check_date_format(cls, values):
        acceptedFormat = "%Y-%m-%d"
        isValidDateFrom = bool(datetime.strptime(values["dateFrom"], acceptedFormat))
        isValidDateTo = bool(datetime.strptime(values["dateTo"], acceptedFormat))
        if not isValidDateFrom or not isValidDateTo:
            raise ValueError('Invalid date format. Date format should be YYYY-MM-DD')
        return values
